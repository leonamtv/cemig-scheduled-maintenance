#!/usr/bin/python

from core.argument_parser import get_city
from core.executing_flow import default_flow


city = get_city()

default_flow(city)
