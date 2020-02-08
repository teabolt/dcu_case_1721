#
# stage 1 of build
#

# build java app using maven
FROM maven:3.5-jdk-8-alpine AS builder

# set app path
WORKDIR /usr/src/app

# install dependencies
COPY pom.xml .
RUN mvn dependency:resolve

# install app
COPY . .
RUN mvn package



#
# stage 2 of build
#

# run the java app using jre
FROM openjdk:8-jre-alpine AS runner

# set path for stage
WORKDIR /usr/src/app

# copy jar files (everything needed is packaged with them)
COPY --from=builder /usr/src/app/target/worker-jar-with-dependencies.jar .

# run app
CMD ["java", "-jar", "worker-jar-with-dependencies.jar"]