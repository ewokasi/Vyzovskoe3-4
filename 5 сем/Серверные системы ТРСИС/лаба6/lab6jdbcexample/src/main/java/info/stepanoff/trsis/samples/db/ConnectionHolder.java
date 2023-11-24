/*
 * this code is available under GNU GPL v3
 * https://www.gnu.org/licenses/gpl-3.0.en.html
 */

package info.stepanoff.trsis.samples.db;

import java.sql.Connection;
import java.sql.PreparedStatement;
import lombok.Data;

/**
 *
 * @author Pavel.Stepanov
 */
@Data
public class ConnectionHolder {
    Connection connection;
    PreparedStatement schoolStatement;
    PreparedStatement deleteSchoolStatement;
    PreparedStatement addSchoolStatement;
    PreparedStatement batchStatement;
}
