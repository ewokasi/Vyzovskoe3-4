package io.swagger.db;

import io.swagger.model.transporters;
import java.util.List;
import org.springframework.data.repository.CrudRepository;
public interface transportersRepository
        extends CrudRepository<transporters, Integer> {
    List<transporters> findByType(Integer type);
}
