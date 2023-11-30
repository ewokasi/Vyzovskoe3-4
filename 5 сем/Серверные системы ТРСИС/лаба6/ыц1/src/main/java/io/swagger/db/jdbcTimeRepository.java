package io.swagger.db;


import io.swagger.model.jdbcTime;
import java.util.List;
import org.springframework.data.repository.CrudRepository;

public interface jdbcTimeRepository extends CrudRepository<jdbcTime, Integer> {
    List<jdbcTime> findByType(Integer type);
}
