package io.swagger.api;

import io.swagger.model.Time;
import io.swagger.model.TimeTable;
import com.fasterxml.jackson.databind.ObjectMapper;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.enums.ParameterIn;
import io.swagger.v3.oas.annotations.media.Schema;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;

import javax.validation.Valid;
import javax.servlet.http.HttpServletRequest;
import java.security.Principal;
import java.sql.SQLException;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;
import io.swagger.model.DBHelper;
import io.swagger.model.ConnectionHolder;
import io.swagger.model.jdbcTime;
import io.swagger.service.jdbcTimeImpl;
@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.SpringCodegen", date = "2023-10-19T16:54:06.552045592Z[GMT]")
@RestController
@RequestMapping("/")
public class TtApiController implements TtApi {

    private static final Logger log = LoggerFactory.getLogger(TtApiController.class);

    private final ObjectMapper objectMapper;

    private final HttpServletRequest request;

    @org.springframework.beans.factory.annotation.Autowired
    public TtApiController(ObjectMapper objectMapper, HttpServletRequest request) {
        this.objectMapper = objectMapper;
        this.request = request;
    }

    private AtomicInteger key = new AtomicInteger();
    public TimeTable TTable = new TimeTable();

   // public Iterable<jdbcTime> jtime = new jdbcTimeImpl().findByType(1);


    public ResponseEntity<Time> createTime(@Parameter(in = ParameterIn.DEFAULT, description = "", required=true, schema=@Schema())  @Valid @RequestBody Time body, @AuthenticationPrincipal Principal principal) throws SQLException {
        String accept = request.getHeader("Accept");
        if (principal == null){
            throw new ForbiddenException();
        }
        if (accept != null && accept.contains("application/json")) {
            synchronized (TTable){
                body.setTimeId(key.incrementAndGet()) ;
                TTable.add(body);
                Integer number = Integer.valueOf(body.getType());
                String name = body.getName();

                DBHelper.addTIMETABLE(number, name);
            }
            return new ResponseEntity<Time>(body, HttpStatus.CREATED);
        }

        return new ResponseEntity<Time>(HttpStatus.NOT_IMPLEMENTED);
    }

    public ResponseEntity<Void> delTime(@Parameter(in = ParameterIn.PATH, description = "Id of Time", required=true, schema=@Schema()) @PathVariable("time_id") int timeId , @AuthenticationPrincipal Principal principal) throws SQLException {

        if (principal == null){
            throw new ForbiddenException();
        }
        TTable.remove(timeId);
        DBHelper.deleteTIMETABLE(timeId);
        return new ResponseEntity<Void>(HttpStatus.OK);
    }

    public ResponseEntity<TimeTable> getTt() throws SQLException {
        String accept = request.getHeader("Accept");

        if (accept != null && accept.contains("application/json")) {

              synchronized (TTable){
                  //System.out.println(jtime);
                  TimeTable tts = DBHelper.getAllTIMETABLEs();
                  return new ResponseEntity<TimeTable>(tts,HttpStatus.OK);
              }


        }

        return new ResponseEntity<TimeTable>(HttpStatus.NOT_IMPLEMENTED);
    }

    public ResponseEntity<Time> getTtById(@Parameter(in = ParameterIn.PATH, description = "Id of Time", required=true, schema=@Schema()) @PathVariable("time_id") int timeId, @AuthenticationPrincipal Principal principal) {
        String accept = request.getHeader("Accept");
        if (principal == null){
            throw new ForbiddenException();
        }
        if (accept != null && accept.contains("application/json")) {
            synchronized (TTable){
                return new ResponseEntity<Time>(TTable.get(timeId),HttpStatus.OK);
            }
        }

        return new ResponseEntity<Time>(HttpStatus.NOT_IMPLEMENTED);
    }

}
