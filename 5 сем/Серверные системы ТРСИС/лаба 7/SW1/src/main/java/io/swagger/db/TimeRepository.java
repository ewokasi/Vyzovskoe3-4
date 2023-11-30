package io.swagger.db;

import io.swagger.model.Time;
import java.util.List;
import org.springframework.data.repository.CrudRepository;
public interface TimeRepository
        extends CrudRepository<Time, Integer> {
    List<Time> findByType(Integer type);
}
