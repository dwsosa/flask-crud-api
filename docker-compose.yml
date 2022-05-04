version: "1.0"
services:
  backend-db:
    image: postgres:alpine
    restart: always
    ports:  
        - 80:5432
    environment:
        - POSTGRES_USER=postgres
        - POSTGRES_PASSWORD=postgres
        - POSTGRES_DB=dealership
        - PGDATA=/var/lib/postgresql/data/
    volumes:
      - ./db:/docker-entrypoint-initdb.d/
