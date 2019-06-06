FROM golang:1.9.2-alpine

WORKDIR /go/src/app

COPY hello-world.go .
RUN apk update && apk add git
RUN go get -u github.com/labstack/echo/...
RUN go build hello-world.go

#CMD ./hello-world
CMD ["go", "run", "hello-world.go"]