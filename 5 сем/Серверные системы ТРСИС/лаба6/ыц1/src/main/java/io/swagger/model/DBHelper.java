/*
 * this code is available under GNU GPL v3
 * https://www.gnu.org/licenses/gpl-3.0.en.html
 */
package io.swagger.model;

import com.google.common.cache.CacheBuilder;
import com.google.common.cache.CacheLoader;
import com.google.common.cache.LoadingCache;
import com.google.common.cache.RemovalListener;
import com.google.common.cache.RemovalNotification;

import com.ibatis.common.resources.Resources;
import io.swagger.model.transporters;
import io.swagger.model.Time;
import lombok.Getter;
import lombok.extern.slf4j.Slf4j;
import org.apache.ibatis.jdbc.ScriptRunner;


import java.io.IOException;
import java.io.Reader;
import java.sql.*;
import java.util.LinkedList;
import java.util.List;
import java.util.concurrent.TimeUnit;

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

    static final String TIMETABLE = "TimeTable";
    static final String TIMETABLE_ID = "TIMETABLE_ID";
    static final String TIMETABLE_TYPE = "TIMETABLE_TYPE";
    static final String TIMETABLE_NAME = "TIMETABLE_NAME";
    static final String TRANSPORTERS = "TRANSPORTERS";
    static final String TRANSPORTERS_ID = "TRANSPORTERS_ID";
    static final String TRANSPORTERS_NUMBER = "TRANSPORTERS_NUMBER";


    static final String SELECT_TIMETABLE_SQL = "SELECT " + TIMETABLE_ID + ",  " + TIMETABLE_TYPE + ",  " + TIMETABLE_NAME + " FROM " + TIMETABLE;
    static final String DELETE_TIMETABLE_SQL = "DELETE FROM " + TIMETABLE + " WHERE " + TIMETABLE_ID + " = ?";
    static final String ADD_TIMETABLE_SQL = "INSERT INTO " + TIMETABLE + " (" + TIMETABLE_TYPE + ", " + TIMETABLE_NAME + ") VALUES (?,?)";


    public static void init() throws IOException, SQLException {
        log.info("init - Instead of @PostConstruct");

        //database init step
        try {
            initialConnection = DriverManager.getConnection(DATABASE_CREATE_URL);

            //ibatis
            ScriptRunner sr = new ScriptRunner(initialConnection);
            Reader reader = Resources.getResourceAsReader("data.sql");

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
                    connectionHolder.setTIMETABLEStatement(connectionHolder.getConnection().prepareStatement(SELECT_TIMETABLE_SQL));
                    connectionHolder.setDeleteTIMETABLEStatement(connectionHolder.getConnection().prepareStatement(DELETE_TIMETABLE_SQL));
                    connectionHolder.setAddTIMETABLEStatement(connectionHolder.getConnection().prepareStatement(ADD_TIMETABLE_SQL, new String[]{TIMETABLE_ID}));


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
                        n.getValue().getTIMETABLEStatement().close();
                        n.getValue().getDeleteTIMETABLEStatement().close();
                        n.getValue().getAddTIMETABLEStatement().close();
                        n.getValue().getTRANSPORTERSStatement().close();
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

    public static TimeTable getAllTIMETABLEs() throws SQLException {


        TimeTable result = new TimeTable();
        while (true) {

            ConnectionHolder connectionHolder = getConnectionHolder();

            synchronized (connectionHolder.getConnection()) {

                PreparedStatement stmt = connectionHolder.getTIMETABLEStatement();

                if (stmt.isClosed()) {
                    continue;
                }
                try (ResultSet rs = stmt.executeQuery()) {
                    while (rs.next()) {
                        int id = rs.getInt(TIMETABLE_ID);
                        int type = rs.getInt(TIMETABLE_TYPE);
                        String name = rs.getString(TIMETABLE_NAME);
                        Time tt = new Time();
                        tt.setName(name);
                        tt.setType(type);
                        tt.setTimeId(id);

                        result.add(tt);
                    }
                }
            }
            System.out.println(result);
            return result;
        }
    }

    public static void deleteTIMETABLE(Integer id) throws SQLException {

        while (true) {

            ConnectionHolder connectionHolder = getConnectionHolder();

            synchronized (connectionHolder.getConnection()) {

                PreparedStatement stmt = connectionHolder.getDeleteTIMETABLEStatement();

                if (stmt.isClosed()) {
                    continue;
                }
                try {
                    stmt.setInt(1, id);
                    stmt.executeUpdate();
                    stmt.getConnection().commit();
                } catch (Exception e) {
                    stmt.getConnection().rollback();
                    log.error("Unable to delete TIMETABLE", e);
                    throw e;
                }
            }
            break;
        }

        log.debug("TIMETABLE with id= " + id + " has been deleted");
    }

    public static Time addTIMETABLE(Integer number, String name) throws SQLException {

        while (true) {

            ResultSet rs1;
            ConnectionHolder connectionHolder = getConnectionHolder();

            synchronized (connectionHolder.getConnection()) {

                PreparedStatement stmt = connectionHolder.getAddTIMETABLEStatement();

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
                        log.debug("Insert into TIMETABLE executed");
                        rs.close();
                        stmt.getConnection().commit();

                        Time fakultet = new Time();
                        fakultet.setName(name);
                        fakultet.setType(number);

                        return fakultet;
                    }
                } catch (Exception e) {
                    stmt.getConnection().rollback();
                    log.error("Unable to add new TIMETABLE", e);
                    throw e;
                }
            }
        }
    }



}
