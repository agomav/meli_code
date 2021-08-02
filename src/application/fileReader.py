#!/usr/bin/python
# -*- coding: utf-8 -*-
#import multiprocessing as mp
from threading import Thread
import queue
import os
from configuration.configProvider import configurationServer
from application.errorReportService import errorGenerator
from domain.fileLoader import fileProcessor



class Reader:
    str_queue= queue.Queue()

    def __init__(self):
        self.err_hand=errorGenerator()


    def read_in_chunks(self,filePath, chunk_size=10):

        file_object = open(filePath)
        while True:
            chunk_data = file_object.read(chunk_size)
            if not chunk_data:
                break
            yield chunk_data

    def proc_file(self,file_location):

        for chunk in self.read_in_chunks(file_location):
            print(chunk)

    def process_wrapper(self, chunkStart, chunkSize, file_location):
        fp = fileProcessor()
        prop = configurationServer()

        with open(file_location) as f:
            f.seek(chunkStart)
            lines = f.read(chunkSize).splitlines()
            for line in lines:

                try:
                    fp._process_line(line)
                    
                    
                except Exception as e:
                    print(e)
                    print ('error reported with the line:' + line)
        print("putting---")            
        self.str_queue.put(self.err_hand.get_full_report())
                    
                    

    def chunkify(self, fname, size=1000):
        fileEnd = os.path.getsize(fname)
        with open(fname, 'rb') as f:
            chunkEnd = f.tell()

            while True:
                chunkStart = chunkEnd
                f.seek(size, 1)
                f.readline()
                chunkEnd = f.tell()
                yield (chunkStart, chunkEnd - chunkStart)
                if chunkEnd > fileEnd:
                    break


    def readFile(self,fileLocation):
       
       response=''
       if os.path.getsize(fileLocation) == 0:
         
          self.err_hand.add_row_error_report('','File loaded is empty. Provide a file with data')
          raise ValueError('Empty file supplied.')

        # init objects

       pool = []
       
       

       # create jobs

       for (chunkStart, chunkSize) in self.chunkify(fileLocation):
            pool.append(Thread(target=self.process_wrapper(chunkStart,chunkSize, fileLocation)))

       
       for tr in pool:
           tr.start()
           response=response+self.str_queue.get()
        
       for trd in pool:
            trd.join()
        
       

       
       
       print("the object has: "+  response )
       #return report
       return response
