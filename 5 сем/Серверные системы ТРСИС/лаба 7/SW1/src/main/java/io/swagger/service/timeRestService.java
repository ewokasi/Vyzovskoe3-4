package io.swagger.service;

import io.swagger.model.Time;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
import java.security.Principal;
import io.swagger.api.ForbiddenException;
import io.swagger.service.TimeService;
import lombok.extern.slf4j.Slf4j;


@Slf4j
@RestController
@RequestMapping("public/rest/time")
public class timeRestService {

    @Autowired
    private TimeService tService;


    @RequestMapping(value = "", method = RequestMethod.GET)
    public ResponseEntity <Iterable<Time>> browse(Principal principal) {
        return ResponseEntity.ok(tService.listAll());
    }

    @RequestMapping(value = "/{id}", method = RequestMethod.DELETE)
    public void delete(@PathVariable("id") Integer id, Principal principal) {
        if (principal == null) {
            throw new ForbiddenException();
        }

        tService.delete(id);
    }

    @RequestMapping(value = "/{id}", method = RequestMethod.GET)
    public ResponseEntity<Time> getOne(@PathVariable("id") Integer id, Principal principal) {
        if (principal == null) {
            throw new ForbiddenException();
        }

        Time TimeById = tService.getById(id);
        if (TimeById == null) {
            return ResponseEntity.notFound().build();
        } else {
            return ResponseEntity.ok(TimeById);
        }
    }

    @RequestMapping(value = "/{name}/{type}", method = RequestMethod.POST)
    public ResponseEntity<Time> add(
                                      @PathVariable("name") String name,
                                      @PathVariable("type") Integer type,
                                      Principal principal) throws Exception {
        if (principal == null) {
            throw new ForbiddenException();
        }

        return ResponseEntity.ok(tService.add(0, name, type));
    }

    @RequestMapping(value = "/search/{type}", method = RequestMethod.GET)
    public ResponseEntity<Iterable<Time>> search(@PathVariable("type") Integer type, Principal principal) {
        if (principal == null) {
            throw new ForbiddenException();
        }

        Iterable<Time> Times = tService.findByType(type);
        return ResponseEntity.ok(Times);
    }
}
