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
@Table(name = "Times")
public class Time {
  public Time(Integer id, String name, Integer type){
    this.id = id;
    this.name = name;
    this.type =  type;
  }
  @Id
//  @Getter
  @GeneratedValue (strategy = GenerationType.IDENTITY)
  @Column(name = "id")
  public Integer id;

  public Time() {

  }

  public void setId(Integer id) {
    this.id = id;
  }
  public Integer GetId(){
    return id;
  }


  @Getter
  @Column(name = "name", unique=true)
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

  public Integer getId(){

    return (this.id);
  }



}
