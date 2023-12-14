package io.swagger.api;

import io.swagger.model.Time;
import io.swagger.service.TimeService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

import javax.validation.Valid;


@Controller
public class timeController {
    @Autowired
    TimeService tService;

    @RequestMapping(value = "/", method = RequestMethod.GET)
    public ModelAndView Time(){

        ModelAndView mav = new ModelAndView("time");
        mav.addObject("Time", tService.listAll());
        return mav;
    }

    @RequestMapping(value = "/time/delete/{id}", method = RequestMethod.DELETE)
    public ModelAndView delete(@PathVariable("id") Integer id) {

        tService.delete(id);
        return new ModelAndView("redirect:/time");
    }

    @RequestMapping(value = "/time/add/{name}/{type}", method = RequestMethod.POST)
    public ModelAndView add(@PathVariable("name") String name,  @PathVariable("type") Integer type) {
        System.out.println("adding") ;
        tService.add(0 ,name, type );
        return new ModelAndView("redirect:/time");
    }


}
