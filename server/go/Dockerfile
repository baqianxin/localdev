FROM golang

MAINTAINER oomcc <baqianxin@163.com>

WORKDIR $GOPATH/src/godocker

ADD . $GOPATH/src/godocker

RUN go build main.go

EXPOSE 8080

ENTRYPOINT ["./main"]