package io.swagger.service;

import io.swagger.db.TimeRepository;
import org.apache.log4j.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import io.swagger.model.Time;

@Service
public class TimeServiceImpl implements TimeService {
    private final static Logger log = Logger.getLogger(TimeServiceImpl.class);

    @Autowired
    private TimeRepository tRep;

    @Override
    public Iterable<Time> findByType(Integer type){
        return tRep.findByType(type);
    }

    @Override
    public Iterable<Time> listAll() {
        return tRep.findAll();
    }

    @Override
    public void delete(Integer id) {
        try {
            tRep.deleteById(id);
        } catch (org.springframework.dao.EmptyResultDataAccessException e) {
        }
    }

    @Override
    public Time add(Integer id, String name, Integer type) {
        return tRep.save(new Time(id, name, type));
    }

    @Override
    public Time getById(Integer id) {
        return tRep.findById(id).orElse(null);
    }

}
