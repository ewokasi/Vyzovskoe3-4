package io.swagger.api;

import io.swagger.service.transportersService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class transportersController {
    @Autowired
    transportersService tService;

    @RequestMapping(value = "/ts/{id}", method = RequestMethod.GET)
    public ModelAndView transporters(@PathVariable("id") Integer id){

        ModelAndView mav = new ModelAndView("ts");
        mav.addObject("transporters", tService.findByType(id));
        return mav;
    }
}
