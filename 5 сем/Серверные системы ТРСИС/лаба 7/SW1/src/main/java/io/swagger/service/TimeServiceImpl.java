package io.swagger.service;
import com.fasterxml.jackson.databind.ObjectMapper;
import io.swagger.db.TimeRepository;
import org.apache.log4j.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Service;
import io.swagger.model.Time;
import io.swagger.kafka.MyKafkaConsumer;
import io.swagger.kafka.MyKafkaProducer;

@Service
public class TimeServiceImpl implements TimeService {
    private final static Logger log = Logger.getLogger(TimeServiceImpl.class);

    private final MyKafkaProducer myKafkaProducer; // сюда блять
    private final MyKafkaConsumer myKafkaConsumer; // сюда блять
    private final ObjectMapper objectMapper = new ObjectMapper();
    @Autowired(required = false)
    public TimeServiceImpl (MyKafkaProducer myKafkaProducer, MyKafkaConsumer myKafkaConsumer){
        this.myKafkaProducer = myKafkaProducer;
        this.myKafkaConsumer = myKafkaConsumer;
    }
    JdbcTemplate jdbcTemplate;
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
    private String convertPatientToMessage(Time recept) {
        try {
            return objectMapper.writeValueAsString(recept);
        } catch (Exception e) {
            throw new RuntimeException("Ошибка при преобразовании Time в сообщение", e);
        }
    }
    @Override
    public Time add(Integer id, String name, Integer type) {
        Time recept_buf = new Time(id, name, type);
        if (myKafkaProducer != null) {
            String message = convertPatientToMessage(recept_buf);
            myKafkaProducer.sendMessage("myTopic", String.valueOf(recept_buf.getId()), message); // сюда блять
//            myKafkaProducer.sendMessage("myTopic", "KAL", message);
        }

        return tRep.save(recept_buf);

    }

    @Override
    public Time getById(Integer id) {
        return tRep.findById(id).orElse(null);
    }

}
