package io.swagger.service;

import io.swagger.model.Time;

public interface TimeService {
    Iterable<Time> findByType(Integer type);

    Iterable<Time> listAll();

    void delete(Integer id);

    Time add(Integer id, String name, Integer Type);

    Time getById(Integer id);


}
