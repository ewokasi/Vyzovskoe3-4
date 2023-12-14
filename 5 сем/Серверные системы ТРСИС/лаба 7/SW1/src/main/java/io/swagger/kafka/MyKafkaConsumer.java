package io.swagger.kafka;

import com.fasterxml.jackson.databind.ObjectMapper;
import io.swagger.db.TimeRepository;
import io.swagger.model.Time;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Profile;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;
import io.swagger.service.TimeServiceImpl;
import io.swagger.db.TimeRepository;

@Service
// @Profile("consumer")
public class MyKafkaConsumer {
    private final TimeRepository repository;
    private final ObjectMapper objectMapper = new ObjectMapper();

    @Autowired
    public MyKafkaConsumer(TimeRepository repository) {
        this.repository = repository;
        System.out.println("MyKafkaConsumer");
    }
    @KafkaListener(topics = "myTopic")
    public void listen(String message) {
        System.out.println(message);
        Time itemObj = convertMessageToItemObj(message);
        repository.save(itemObj);
    }
    private Time convertMessageToItemObj(String message) {
        try {
            return objectMapper.readValue(message, Time.class);
        } catch (Exception e) {
            throw new RuntimeException("Ошибка при преобразовании сообщения", e);
        }
    }
}