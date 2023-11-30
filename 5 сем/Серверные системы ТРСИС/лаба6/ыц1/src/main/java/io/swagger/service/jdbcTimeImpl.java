package io.swagger.service;


import io.swagger.db.jdbcTimeRepository;
import org.apache.log4j.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import io.swagger.model.jdbcTime;

@Service
public class jdbcTimeImpl implements jdbcTimeService {
    private final static Logger log = Logger.getLogger(transportersServiceImpl.class);

    @Autowired
    private jdbcTimeService tRep;

    @Override
    public Iterable<jdbcTime> findByType(Integer type){
        return tRep.findByType(type);
    }
}
