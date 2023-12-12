FROM openjdk:17

RUN mkdir -p /usr/src/myapp
COPY target/swagger-spring-1.0.0.jar /usr/src/myapp
RUN mkdir -p /usr/src/myapp/target
COPY target/keystore.p12 /usr/src/myapp/target
WORKDIR /usr/src/myapp
ARG JAR_FILE=target/swagger-spring-1.0.0.jar
ADD ${JAR_FILE} app.jar
ENTRYPOINT ["java", "-jar","app.jar"]
