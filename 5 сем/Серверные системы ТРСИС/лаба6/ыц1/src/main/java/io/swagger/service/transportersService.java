package io.swagger.service;

import io.swagger.model.transporters;

public interface transportersService {
    Iterable<transporters> findByType(Integer type);
}
