MCP Client-Server System

Overview

This project implements an MCP-based Client-Server System where a client sends a query, the server processes it using Ollama LLM, generates a system command, executes it, and returns the output. The implementation uses FastAPI, FastMCP, aiohttp, and subprocess for command execution.

Installation

Prerequisites

Python 3.8+

Pip package manager

Ollama installed and running

MCP Python SDK installed

Setup

Clone the repository:

>>> cd mcp_server_client_assessment

Install dependencies:

>>> pip install -r requirements.txt

Start the server:

>>> python server.py

Run the client:

>>> python client.py
