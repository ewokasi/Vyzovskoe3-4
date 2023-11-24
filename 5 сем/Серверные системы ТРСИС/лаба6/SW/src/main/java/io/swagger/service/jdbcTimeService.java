package io.swagger.service;

import io.swagger.model.jdbcTime;

public interface jdbcTimeService {
    Iterable<jdbcTime> findByType(Integer type);
}
