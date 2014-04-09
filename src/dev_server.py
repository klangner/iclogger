# -*- coding: utf-8 -*-
'''
Created on 2014-04-09

@author: Krzysztof Langner
'''
# import iclogger.file_logger as Logger
import iclogger.dynamodb_logger as Logger


if __name__ == "__main__":
    Logger.app.run(debug=True)