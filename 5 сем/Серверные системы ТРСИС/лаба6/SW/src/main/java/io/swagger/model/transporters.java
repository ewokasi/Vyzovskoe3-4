package io.swagger.model;

import io.swagger.models.auth.In;
import lombok.Getter;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name = "transporters")
public class transporters {
   public transporters(Integer id, String name, Integer type){
       this.id = id;
       this.name = name;
       this.type =  type;
   }
   @Id
   @GeneratedValue (strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private Integer id;

    public transporters() {

    }

    public void setId(Integer id) {
        this.id = id;
    }
    public Integer GetId(){
        return id;
    }


    @Getter
    @Column(name = "name")
    private String name;

    public void setName(String name) {
        this.name = name;
    }

    @Getter
    @Column(name = "type")
    private Integer type;

    public void setType(Integer type) {
        this.type = type;
    }
}
