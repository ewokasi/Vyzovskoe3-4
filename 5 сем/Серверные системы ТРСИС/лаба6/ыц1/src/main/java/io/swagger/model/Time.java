package io.swagger.model;

import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonCreator;
import io.swagger.v3.oas.annotations.media.Schema;
import org.springframework.validation.annotation.Validated;
import javax.validation.Valid;
import javax.validation.constraints.*;

/**
 * Time
 */
@Validated
@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.SpringCodegen", date = "2023-10-19T16:54:06.552045592Z[GMT]")


public class Time  {


  @JsonProperty("time_id")
  private int timeId = 0;

  @JsonProperty("name")
  private String name = null;

  @JsonProperty("type")
  private int type = 0;

  public Time timeId(int timeId) {
    this.timeId = timeId;
    return this;
  }

  /**
   * Get timeId
   * @return timeId
   **/
  @Schema(description = "")
  
    public int getTimeId() {
    return timeId;
  }

  public void setTimeId(int timeId) {
    this.timeId = timeId;
  }

  public Time name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Get name
   * @return name
   **/
  @Schema(required = true, description = "")
      @NotNull

    public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public Time type(int type) {
    this.type = type;
    return this;
  }

  /**
   * Get type
   * @return type
   **/
  @Schema(description = "")
  
    public int getType() {
    return type;
  }

  public void setType(int type) {
    this.type = type;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Time time = (Time) o;
    return Objects.equals(this.timeId, time.timeId) &&
        Objects.equals(this.name, time.name) &&
        Objects.equals(this.type, time.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(timeId, name, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Time {\n");
    
    sb.append("    timeId: ").append(toIndentedString(timeId)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }
}
