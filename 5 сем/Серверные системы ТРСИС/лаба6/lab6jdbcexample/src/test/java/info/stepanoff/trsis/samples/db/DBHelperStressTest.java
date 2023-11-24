/*
 * this code is available under GNU GPL v3
 * https://www.gnu.org/licenses/gpl-3.0.en.html
 */
/**
 *
 * @author Pavel.Stepanov
 */
package info.stepanoff.trsis.samples.db;

import info.stepanoff.trsis.samples.db.model.Batch;
import java.sql.SQLException;
import java.time.Duration;
import java.time.Instant;
import java.time.temporal.ChronoUnit;
import java.time.temporal.TemporalUnit;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.atomic.AtomicInteger;
import lombok.extern.slf4j.Slf4j;
import static org.junit.Assert.*;
import org.junit.Test;

/**
 *
 * @author Pavel
 */
@Slf4j
public class DBHelperStressTest {

    AtomicInteger schoolNumber = new AtomicInteger(100);
    volatile static boolean pass = true;

    @Test
    public void testAddDeleteSchool() throws Exception {
        log.info("addSchool then deleteSchool stress test");

        Instant now = Instant.now();

        class WorkerThread implements Runnable {

            @Override
            public void run() {

                try {
                    int num = schoolNumber.incrementAndGet();
                    String name = "test" + num;
                    Integer id = DBHelper.addSchool(num, name).getId();
                    List<Batch> batchBySchool = DBHelper.getBatchBySchool(id);

                    DBHelper.deleteSchool(id);

                    if (num % 100000 == 0) //to avoid suppression of this message by logback-test.xml settings
                    {
                        Instant newNow = Instant.now();

                        log.info("Performed test #"
                                + num
                                + " rate "
                                + num / Duration.between(now, newNow).getSeconds()
                                + " scenarios per second");
                    }

                } catch (SQLException ex) {
                    log.error("Error executing SQL Statement", ex);
                    pass = false;
                    fail("SQL error executing stress test");
                }
            }
        }

        DBHelper.init();

        ExecutorService executor = Executors.newFixedThreadPool(100);
        for (int i = 0; i < 1000000; i++) {
            Runnable worker = new WorkerThread();
            executor.execute(worker);
        }

        executor.shutdown();

        while (!executor.isTerminated());

        if (!pass) {
            fail("Exception in one of worker threads");
        }
        log.info("Finished executing stress test");

    }

}
