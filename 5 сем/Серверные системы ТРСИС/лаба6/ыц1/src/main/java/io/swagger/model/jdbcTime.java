package io.swagger.model;
import io.swagger.models.auth.In;
import lombok.Getter;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;
@Getter
@Entity
@Table(name = "jdbcTime")
public class jdbcTime {
    public jdbcTime(Integer id, String name, Integer type){
        this.id = id;
        this.name = name;
        this.type =  type;
    }
    @Id
    private int id;

    public jdbcTime() {

    }

    public void setId(int id) {
        this.id = id;
    }

    @Column(name = "name")
    private String name;

    public void setName(String name) {
        this.name = name;
    }

    @Column(name = "type")
    private Integer type;

    public void setType(Integer type) {
        this.type = type;
    }
}
