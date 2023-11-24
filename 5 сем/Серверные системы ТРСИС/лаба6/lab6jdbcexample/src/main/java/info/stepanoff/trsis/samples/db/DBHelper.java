/*
 * this code is available under GNU GPL v3
 * https://www.gnu.org/licenses/gpl-3.0.en.html
 */
package info.stepanoff.trsis.samples.db;

import com.google.common.cache.CacheBuilder;
import com.google.common.cache.CacheLoader;
import com.google.common.cache.LoadingCache;
import com.google.common.cache.RemovalListener;
import com.google.common.cache.RemovalNotification;
import info.stepanoff.trsis.samples.db.model.Batch;
import info.stepanoff.trsis.samples.db.model.School;
import java.io.IOException;
import java.io.Reader;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.LinkedList;
import java.util.List;
import java.util.concurrent.TimeUnit;
import lombok.Getter;
import lombok.extern.slf4j.Slf4j;
import org.apache.ibatis.io.Resources;
import org.apache.ibatis.jdbc.ScriptRunner;

/**
 *
 * @author Pavel
 */
@Slf4j
public class DBHelper {

    static Connection conn;

    static final String DATABASE_URL = "jdbc:h2:mem:testdb";
    static final String DATABASE_CREATE_URL = DATABASE_URL + "";

    static final int NUMBER_OF_CONNECTIONS = 30;
    static volatile int currentConnection = 0;

    private static CacheLoader<Integer, ConnectionHolder> loader;
    private static LoadingCache<Integer, ConnectionHolder> cache;
    private static RemovalListener<Integer, ConnectionHolder> listener;

    @Getter
    private static Connection initialConnection;

    static final String SCHOOL = "SCHOOL";
    static final String SCHOOL_ID = "SCHOOL_ID";
    static final String SCHOOL_NUMBER = "SCHOOL_NUMBER";
    static final String SCHOOL_NAME = "SCHOOL_NAME";
    static final String BATCH = "BATCH";
    static final String BATCH_ID = "BATCH_ID";
    static final String BATCH_NUMBER = "BATCH_NUMBER";
    static final String BATCH_SCHOOL_ID = "BATCH_SCHOOL_ID";

    static final String SELECT_SCHOOL_SQL = "SELECT " + SCHOOL_ID + ",  " + SCHOOL_NUMBER + ",  " + SCHOOL_NAME + " FROM " + SCHOOL;
    static final String DELETE_SCHOOL_SQL = "DELETE FROM " + SCHOOL + " WHERE " + SCHOOL_ID + " = ?";
    static final String ADD_SCHOOL_SQL = "INSERT INTO " + SCHOOL + " (" + SCHOOL_NUMBER + ", " + SCHOOL_NAME + ") VALUES (?,?)";
    static final String SELECT_BATCH_SQL = "SELECT " + BATCH_ID + ",  " + BATCH_NUMBER + " FROM " + BATCH + " WHERE " + BATCH_SCHOOL_ID + " = ?";

    public static void init() throws IOException, SQLException {
        log.info("init - Instead of @PostConstruct");

        //database init step
        try {
            initialConnection = DriverManager.getConnection(DATABASE_CREATE_URL);

            //ibatis
            ScriptRunner sr = new ScriptRunner(initialConnection);
            Reader reader = Resources.getResourceAsReader("init.sql");

            // Exctute script
            sr.runScript(reader);

            reader = Resources.getResourceAsReader("fill.sql");

            // Exctute script
            sr.runScript(reader);
        } catch (SQLException | IOException ex) {
            log.error("Critical failure - impossible to continue correctly");
            throw ex;
        }

        //Init cache loader. Code is used to create new connections and statements
        loader = new CacheLoader<Integer, ConnectionHolder>() {
            @Override
            public ConnectionHolder load(Integer key) {
                try {
                    ConnectionHolder connectionHolder = new ConnectionHolder();
                    log.info("Creating new ConnectionHolder for key " + key);
                    connectionHolder.setConnection(DriverManager.getConnection(DATABASE_URL));
                    connectionHolder.getConnection().setAutoCommit(false);
                    connectionHolder.setSchoolStatement(connectionHolder.getConnection().prepareStatement(SELECT_SCHOOL_SQL));
                    connectionHolder.setDeleteSchoolStatement(connectionHolder.getConnection().prepareStatement(DELETE_SCHOOL_SQL));
                    connectionHolder.setAddSchoolStatement(connectionHolder.getConnection().prepareStatement(ADD_SCHOOL_SQL, new String[]{SCHOOL_ID}));
                    connectionHolder.setBatchStatement(connectionHolder.getConnection().prepareStatement(SELECT_BATCH_SQL));

                    return connectionHolder;
                } catch (SQLException e) {
                    log.error("Exception getting connection to database", e);
                    return null;
                }
            }
        };

        //Eviction listener. Code is used to close expired connections
        listener = new RemovalListener<Integer, ConnectionHolder>() {
            @Override
            public void onRemoval(RemovalNotification<Integer, ConnectionHolder> n) {
                try {
                    synchronized (n.getValue().getConnection()) {
                        log.info("Closing old connection for key " + n.getKey());
                        n.getValue().getSchoolStatement().close();
                        n.getValue().getDeleteSchoolStatement().close();
                        n.getValue().getAddSchoolStatement().close();
                        n.getValue().getBatchStatement().close();
                        n.getValue().getConnection().commit();
                        n.getValue().getConnection().close();
                    }
                } catch (SQLException ex) {
                    log.error("Exception closing connection to database", ex);
                }
            }
        };

        cache = CacheBuilder.newBuilder().refreshAfterWrite(10, TimeUnit.SECONDS).removalListener(listener).build(loader);
    }

    private static ConnectionHolder getConnectionHolder() throws SQLException {
        currentConnection = (currentConnection + 1) % NUMBER_OF_CONNECTIONS;
        return cache.getUnchecked(currentConnection);
    }

    public static List<School> getAllSchools() throws SQLException {

        List<School> result = new LinkedList<>();
        while (true) {

            ConnectionHolder connectionHolder = getConnectionHolder();

            synchronized (connectionHolder.getConnection()) {

                PreparedStatement stmt = connectionHolder.getSchoolStatement();

                if (stmt.isClosed()) {
                    continue;
                }
                try (ResultSet rs = stmt.executeQuery()) {
                    while (rs.next()) {
                        int id = rs.getInt(SCHOOL_ID);
                        int nomer = rs.getInt(SCHOOL_NUMBER);
                        String imya = rs.getString(SCHOOL_NAME);
                        School fakultet = new School(id, nomer, imya);

                        result.add(fakultet);
                    }
                }
            }
            return result;
        }
    }

    public static void deleteSchool(Integer id) throws SQLException {

        while (true) {

            ConnectionHolder connectionHolder = getConnectionHolder();

            synchronized (connectionHolder.getConnection()) {

                PreparedStatement stmt = connectionHolder.getDeleteSchoolStatement();

                if (stmt.isClosed()) {
                    continue;
                }
                try {
                    stmt.setInt(1, id);
                    stmt.executeUpdate();
                    stmt.getConnection().commit();
                } catch (Exception e) {
                    stmt.getConnection().rollback();
                    log.error("Unable to delete school", e);
                    throw e;
                }
            }
            break;
        }

        log.debug("school with id= " + id + " has been deleted");
    }

    public static School addSchool(Integer number, String name) throws SQLException {

        while (true) {

            ResultSet rs1;
            ConnectionHolder connectionHolder = getConnectionHolder();

            synchronized (connectionHolder.getConnection()) {

                PreparedStatement stmt = connectionHolder.getAddSchoolStatement();

                if (stmt.isClosed()) {
                    continue;
                }
                try {
                    stmt.setInt(1, number);
                    stmt.setString(2, name);
                    stmt.executeUpdate();
                    rs1 = stmt.getGeneratedKeys();

                    try (ResultSet rs = rs1) {
                        rs.next();
                        Integer key = rs.getInt(1);
                        log.debug("Insert into School executed");
                        rs.close();
                        stmt.getConnection().commit();
                        return new School(key, number, name);
                    }
                } catch (Exception e) {
                    stmt.getConnection().rollback();
                    log.error("Unable to add new school", e);
                    throw e;
                }
            }
        }
    }

    public static List<Batch> getBatchBySchool(Integer schoolId) throws SQLException {

        List<Batch> result = new LinkedList<>();

        while (true) {

            ConnectionHolder connectionHolder = getConnectionHolder();

            synchronized (connectionHolder.getConnection()) {

                PreparedStatement stmt = connectionHolder.getBatchStatement();

                if (stmt.isClosed()) {
                    continue;
                }

                stmt.setInt(1, schoolId);

                log.debug("getBatchBySchool query executed");

                try (ResultSet rs = stmt.executeQuery()) {
                    while (rs.next()) {

                        int id = rs.getInt(BATCH_ID);
                        String number = rs.getString(BATCH_NUMBER);

                        Batch batch = new Batch(id, number);

                        result.add(batch);

                    }
                }
            }
            break;
        }
        return result;
    }

}
