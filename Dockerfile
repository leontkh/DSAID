FROM postgres:latest

ENV POSTGRES_USER postgres_user
ENV POSTGRES_PASSWORD postgres_pw
ENV POSTGRES_DB postgres_db

COPY ./initdb/ /docker-entrypoint-initdb.d/
RUN chown -R postgres:postgres /docker-entrypoint-initdb.d/
EXPOSE 5432

CMD ["docker-entrypoint.sh", "postgres"]
