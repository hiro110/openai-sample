# Use the Python base image
FROM python:3.11.2-bullseye AS builder

RUN pip install langchain && pip install openai && mkdir -p /var/app/langchain

WORKDIR /var/app/langchain