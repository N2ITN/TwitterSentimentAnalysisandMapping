import os, time
#os.chdir('/'.join(__file__.split('/')[:-1]))
from TwitMapFeel import spamfilter_georefrence_topicfilter as sg
from TwitMapFeel import parse_json as pj
start = time.time()


inputFile = r"C:\Users\zeste\Documents\GitHub\TwitterSentimentAnalysisandMapping\TwitMapFeel\output_un.txt"
outputFile = r"clean_dataSeattle3.json"
print("GOT:" + inputFile)
def parse(inputFile=inputFile,outputFile=outputFile):
    pj.ExportCleanData(inputFile, outputFile)

# parse()
tweets_data_path = r"C:\Users\zeste\Documents\GitHub\TwitterSentimentAnalysisandMapping\clean_dataSeattle3.json"

#filter_out = [ '#MassTransitNow', '#ST3', 'proposition 1', 'sound transit 3', 'Sound Transit', 'Prop 1']
#allTweets = sg.Filter_OutSpam_ByTopics_ByPopularity(tweets_data_path)
#print(allTweets.DescribeData())

# allDF = allTweets.ReturnData()
# print(allDF)
# sentimentAnalysis = sg.Sentiment(allDF, latitude=17.616614, longitude=-122.334540)

# #Maps
# map1 = sentimentAnalysis.MapIndividualTweets()
# #map2 = sentimentAnalysis.MapAggregatedTweets()

# neigborhoodSentiment = sentimentAnalysis.NeighborhoodSentiment(allDF)
# print(neigborhoodSentiment)

#Look at elapsed time of program
end = time.time()
print(("\n" + "elapsed time:" + str(end - start)))
