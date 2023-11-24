/*
 * this code is available under GNU GPL v3
 * https://www.gnu.org/licenses/gpl-3.0.en.html
 */

package io.swagger.model;

import lombok.Data;

import java.sql.Connection;
import java.sql.PreparedStatement;

/**
 *
 * @author Pavel.Stepanov
 */
@Data
public class ConnectionHolder {
    Connection connection;
    PreparedStatement TIMETABLEStatement;
    PreparedStatement deleteTIMETABLEStatement;
    PreparedStatement addTIMETABLEStatement;
    PreparedStatement TRANSPORTERSStatement;
}
