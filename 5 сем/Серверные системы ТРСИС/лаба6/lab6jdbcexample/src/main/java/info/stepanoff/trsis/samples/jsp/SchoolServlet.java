/*
 * this code is available under GNU GPL v3
 * https://www.gnu.org/licenses/gpl-3.0.en.html
 */

package info.stepanoff.trsis.samples.jsp;

import info.stepanoff.trsis.samples.db.DBHelper;
import info.stepanoff.trsis.samples.db.model.School;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.sql.SQLException;
import java.util.logging.Level;
import java.util.logging.Logger;

public class SchoolServlet extends javax.servlet.http.HttpServlet {

    private static final long serialVersionUID = 1L;

    private final String responseTemplate1
            = "<html>\n"
            + "<body>\n"
            + "<h2>List of schools</h2>\n"
            + "<table> \n"
            + "<thead><th>Number</th><th>Name</th><th>Action</th></thead>\n"
            + "<tbody>\n";

    private final String responseTemplate2
            = "</tbody></table>\n"
            + "<form method='post' accept-charset=\"UTF-8\"><input name='command' type='hidden' value='add'>Number of school<br><input name='number'><br>Name of school<br><input name='name'><br><input type='submit' value='Add'></form></body>\n"
            + "</body>\n"
            + "</html>";

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException {
        try {
            process(request, response);
        } catch (SQLException ex) {
            Logger.getLogger(SchoolServlet.class.getName()).log(Level.SEVERE, null, ex);
            throw new IOException(ex);
        }
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException {
        try {
            process(request, response);
        } catch (SQLException ex) {
            Logger.getLogger(SchoolServlet.class.getName()).log(Level.SEVERE, null, ex);
            throw new IOException(ex);
        }
    }

    private void process(HttpServletRequest request, HttpServletResponse response) throws IOException, SQLException {

        //Browsers have problems using methods other than get and post in forms; so we are using post and special attribute to indicate command
        String command = request.getParameter("command");
        if (command != null) {
            switch (command) {
                case "delete":
                    Integer id = Integer.valueOf(request.getParameter("id"));
                    DBHelper.deleteSchool(id);
                    response.sendRedirect("school");
                    break;
                case "add":
                    Integer number = Integer.valueOf(request.getParameter("number"));
                    String name = request.getParameter("name");
                    name = new String(name.getBytes("iso-8859-1"), "UTF-8");
                    DBHelper.addSchool(number, name);
                    break;
            }
        }

        response.setStatus(200);
        response.setContentType("text/html;charset=UTF-8");

        response.getWriter().write(responseTemplate1);

        for (School fakultet : DBHelper.getAllSchools()) {
            response.getWriter().write("<tr>");
            response.getWriter().write("<td>");
            response.getWriter().write(fakultet.getNumber().toString());
            response.getWriter().write("</td>");
            response.getWriter().write("<td>");
            response.getWriter().write("<a href=\"batch?school=" + fakultet.getId().toString() + "\">");
            response.getWriter().write(fakultet.getName());
            response.getWriter().write("</a>");
            response.getWriter().write("</td>");
            response.getWriter().write("<td>");
            response.getWriter().write("<a href=\"school?command=delete&id=" + fakultet.getId().toString() + "\">delete</a>");
            response.getWriter().write("</td>");
            response.getWriter().write("</tr>");
        }
        response.getWriter().write(responseTemplate2);
    }

}
