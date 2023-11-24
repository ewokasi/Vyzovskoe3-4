package io.swagger.service;

import io.swagger.db.transportersRepository;
import org.apache.log4j.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import io.swagger.model.transporters;

@Service
public class transportersServiceImpl implements transportersService {
    private final static Logger log = Logger.getLogger(transportersServiceImpl.class);

    @Autowired
    private transportersRepository tRep;

    @Override
    public Iterable<transporters> findByType(Integer type){
        return tRep.findByType(type);
    }
}
