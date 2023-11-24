package io.swagger.api;

import io.swagger.model.Error;
import io.swagger.model.Time;
import io.swagger.model.TimeTable;
import com.fasterxml.jackson.databind.ObjectMapper;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.enums.ParameterIn;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.media.ArraySchema;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.media.Schema;
import io.swagger.v3.oas.annotations.security.SecurityRequirement;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.CookieValue;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RequestPart;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import javax.validation.Valid;
import javax.validation.constraints.*;
import javax.servlet.http.HttpServletRequest;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.concurrent.atomic.AtomicInteger;

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.SpringCodegen", date = "2023-10-19T16:54:06.552045592Z[GMT]")
@RestController
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
    public ResponseEntity<TimeTable> createTime(@Parameter(in = ParameterIn.DEFAULT, description = "", required=true, schema=@Schema()) @Valid @RequestBody Time body) {
        String accept = request.getHeader("Accept");
        if (accept != null && accept.contains("application/json")) {
            synchronized (TTable){
                body.setTimeId(key.incrementAndGet()) ;
                TTable.add(body);
            }
            return new ResponseEntity<TimeTable>(HttpStatus.CREATED);
        }

        return new ResponseEntity<TimeTable>(HttpStatus.NOT_IMPLEMENTED);
    }

    public ResponseEntity<Void> delTime(@Parameter(in = ParameterIn.PATH, description = "Id of Time", required=true, schema=@Schema()) @PathVariable("time_id") int timeId) {
        String accept = request.getHeader("Accept");
        TTable.remove(timeId);
        return new ResponseEntity<Void>(HttpStatus.OK);
    }

    public ResponseEntity<TimeTable> getTt() {
        String accept = request.getHeader("Accept");
        if (accept != null && accept.contains("application/json")) {
                System.out.println("con");
              synchronized (TTable){
                  return new ResponseEntity<TimeTable>(TTable,HttpStatus.OK);
              }


        }

        return new ResponseEntity<TimeTable>(HttpStatus.NOT_IMPLEMENTED);
    }

    public ResponseEntity<Time> getTtById(@Parameter(in = ParameterIn.PATH, description = "Id of Time", required=true, schema=@Schema()) @PathVariable("time_id") int timeId) {
        String accept = request.getHeader("Accept");
        if (accept != null && accept.contains("application/json")) {
            synchronized (TTable){
                return new ResponseEntity<Time>(TTable.get(timeId),HttpStatus.OK);
            }
        }

        return new ResponseEntity<Time>(HttpStatus.NOT_IMPLEMENTED);
    }

}
