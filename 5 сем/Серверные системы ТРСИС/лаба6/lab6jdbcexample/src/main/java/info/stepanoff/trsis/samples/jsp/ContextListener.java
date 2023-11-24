/*
 * this code is available under GNU GPL v3
 * https://www.gnu.org/licenses/gpl-3.0.en.html
 */

package info.stepanoff.trsis.samples.jsp;

import javax.servlet.ServletContextEvent;
import javax.servlet.ServletContextListener;
import javax.servlet.annotation.WebListener;
import info.stepanoff.trsis.samples.db.DBHelper;
import java.io.IOException;
import java.sql.SQLException;
import lombok.extern.slf4j.Slf4j;


@WebListener
@Slf4j
public class ContextListener implements ServletContextListener {

    @Override
    public void contextInitialized(ServletContextEvent sce) {

        try {
            //start database
            DBHelper.init();
            
        } catch (SQLException | IOException ex) {
            log.error("Exception in context initialized listener",ex);
        }
    }

    @Override
    public void contextDestroyed(ServletContextEvent sce) {
        try {
            //stop database
            DBHelper.getInitialConnection().close();
        } catch (SQLException ex) {
            log.error("Exception in context destroyed listener",ex);
        }
    }

}
