/**
 * NOTE: This class is auto generated by the swagger code generator program (3.0.48).
 * https://github.com/swagger-api/swagger-codegen
 * Do not edit the class manually.
 */
package io.swagger.api;

import io.swagger.model.Error;
import io.swagger.model.Time;
import io.swagger.model.TimeTable;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.enums.ParameterIn;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.media.ArraySchema;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.media.Schema;
import io.swagger.v3.oas.annotations.security.SecurityRequirement;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RequestPart;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.bind.annotation.CookieValue;

import javax.validation.Valid;
import javax.validation.constraints.*;
import java.util.List;
import java.util.Map;

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.SpringCodegen", date = "2023-10-19T16:54:06.552045592Z[GMT]")
@Validated
public interface TtApi {

    @Operation(summary = "добавить в расписание", description = "", tags={ "tt" })
    @ApiResponses(value = { 
        @ApiResponse(responseCode = "200", description = "Успех", content = @Content(mediaType = "application/json", schema = @Schema(implementation = TimeTable.class))),
        
        @ApiResponse(responseCode = "200", description = "Error", content = @Content(mediaType = "application/json", schema = @Schema(implementation = Error.class))) })
    @RequestMapping(value = "/tt",
        produces = { "application/json" }, 
        consumes = { "application/json" }, 
        method = RequestMethod.POST)
    ResponseEntity<TimeTable> createTime(@Parameter(in = ParameterIn.DEFAULT, description = "", required=true, schema=@Schema()) @Valid @RequestBody Time body);


    @Operation(summary = "удаление", description = "", tags={ "tt" })
    @ApiResponses(value = { 
        @ApiResponse(responseCode = "200", description = "Успех"),
        
        @ApiResponse(responseCode = "200", description = "Error", content = @Content(mediaType = "application/json", schema = @Schema(implementation = Error.class))) })
    @RequestMapping(value = "/tt/{time_id}",
        produces = { "application/json" }, 
        method = RequestMethod.DELETE)
    ResponseEntity<Void> delTime(@Parameter(in = ParameterIn.PATH, description = "Id of Time", required=true, schema=@Schema()) @PathVariable("time_id") int timeId);


    @Operation(summary = "получить расписание", description = "", tags={ "tt" })
    @ApiResponses(value = { 
        @ApiResponse(responseCode = "200", description = "Успех", content = @Content(mediaType = "application/json", schema = @Schema(implementation = TimeTable.class))),
        
        @ApiResponse(responseCode = "200", description = "Error", content = @Content(mediaType = "application/json", schema = @Schema(implementation = Error.class))) })
    @RequestMapping(value = "/tt",
        produces = { "application/json" }, 
        method = RequestMethod.GET)
    ResponseEntity<TimeTable> getTt();


    @Operation(summary = "по id", description = "", tags={ "tt" })
    @ApiResponses(value = { 
        @ApiResponse(responseCode = "200", description = "Успех", content = @Content(mediaType = "application/json", schema = @Schema(implementation = Time.class))),
        
        @ApiResponse(responseCode = "200", description = "Error", content = @Content(mediaType = "application/json", schema = @Schema(implementation = Error.class))) })
    @RequestMapping(value = "/tt/{time_id}",
        produces = { "application/json" }, 
        method = RequestMethod.GET)
    ResponseEntity<Time> getTtById(@Parameter(in = ParameterIn.PATH, description = "Id of Time", required=true, schema=@Schema()) @PathVariable("time_id") int timeId);

}

