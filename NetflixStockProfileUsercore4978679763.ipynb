{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Introduction\n",
    "\n",
    "In this project, you will act as a data visualization developer at Yahoo Finance! You will be helping the \"Netflix Stock Profile\" team visualize the Netflix stock data. In finance, a _stock profile_ is a series of studies, visualizations, and analyses that dive into different aspects a publicly traded company's data. \n",
    "\n",
    "For the purposes of the project, you will only visualize data for the year of 2017. Specifically, you will be in charge of creating the following visualizations:\n",
    "+ The distribution of the stock prices for the past year\n",
    "+ Netflix's earnings and revenue in the last four quarters\n",
    "+ The actual vs. estimated earnings per share for the four quarters in 2017\n",
    "+ A comparison of the Netflix Stock price vs the Dow Jones Industrial Average price in 2017 \n",
    "\n",
    "Note: We are using the Dow Jones Industrial Average to compare the Netflix stock to the larter stock market. Learn more about why the Dow Jones Industrial Average is a general reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp).\n",
    "\n",
    "During this project, you will analyze, prepare, and plot data. Your visualizations will help the financial analysts asses the risk of the Netflix stock.\n",
    "\n",
    "After you complete your visualizations, you'll be creating a presentation to share the images with the rest of the Netflix Stock Profile team. Your slides should include:\n",
    "\n",
    "- A title slide\n",
    "- A list of your visualizations and your role in their creation for the \"Stock Profile\" team\n",
    "- A visualization of the distribution of the stock prices for Netflix in 2017\n",
    "- A visualization and a summary of Netflix stock and revenue for the past four quarters and a summary\n",
    "- A visualization and a brief summary of their earned versus actual earnings per share\n",
    "- A visualization of Netflix stock against the Dow Jones stock (to get a sense of the market) in 2017\n",
    "\n",
    "Financial Data Source: [Yahoo Finance](https://finance.yahoo.com/quote/DATA/)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 1\n",
    "\n",
    "Let's get our notebook ready for visualizing! Import the modules that you'll be using in this project:\n",
    "- `from matplotlib import pyplot as plt`\n",
    "- `import pandas as pd`\n",
    "- `import seaborn as sns`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {},
   "outputs": [],
   "source": [
    "from matplotlib import pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [],
   "source": [
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's load the datasets and inspect them."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Load **NFLX.csv** into a DataFrame called `netflix_stocks`. Then, quickly inspect the DataFrame using `print()`.\n",
    "\n",
    "Hint: Use the `pd.read_csv()`function).\n",
    "\n",
    "Note: In the Yahoo Data, `Adj Close` represents the adjusted close price adjusted for both dividends and splits. This means this is the true closing stock price for a given business day."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {},
   "outputs": [],
   "source": [
    "netflix_stocks = pd.read_csv('NFLX.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          Date        Open        High         Low       Close   Adj Close  \\\n",
      "0   2017-01-01  124.959999  143.460007  124.309998  140.710007  140.710007   \n",
      "1   2017-02-01  141.199997  145.949997  139.050003  142.130005  142.130005   \n",
      "2   2017-03-01  142.839996  148.289993  138.259995  147.809998  147.809998   \n",
      "3   2017-04-01  146.699997  153.520004  138.660004  152.199997  152.199997   \n",
      "4   2017-05-01  151.910004  164.750000  151.610001  163.070007  163.070007   \n",
      "5   2017-06-01  163.520004  166.869995  147.300003  149.410004  149.410004   \n",
      "6   2017-07-01  149.800003  191.500000  144.250000  181.660004  181.660004   \n",
      "7   2017-08-01  182.490005  184.619995  164.229996  174.710007  174.710007   \n",
      "8   2017-09-01  175.550003  189.949997  172.440002  181.350006  181.350006   \n",
      "9   2017-10-01  182.110001  204.380005  176.580002  196.429993  196.429993   \n",
      "10  2017-11-01  197.240005  202.479996  184.320007  195.509995  195.509995   \n",
      "11  2017-12-01  186.990005  194.490005  178.380005  191.960007  191.960007   \n",
      "\n",
      "       Volume  \n",
      "0   181772200  \n",
      "1    91432000  \n",
      "2   110692700  \n",
      "3   149769200  \n",
      "4   116795800  \n",
      "5   135675800  \n",
      "6   185144700  \n",
      "7   136523100  \n",
      "8   111427900  \n",
      "9   208657800  \n",
      "10  161719700  \n",
      "11  115103700  \n"
     ]
    }
   ],
   "source": [
    "print(netflix_stocks)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Load **DJI.csv** into a DataFrame called `dowjones_stocks`. Then, quickly inspect the DataFrame using `print()`.\n",
    "\n",
    "Note: You can learn more about why the Dow Jones Industrial Average is a industry reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp). \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {},
   "outputs": [],
   "source": [
    "dowjones_stocks = pd.read_csv('DJI.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          Date          Open          High           Low         Close  \\\n",
      "0   2017-01-01  19872.859375  20125.580078  19677.939453  19864.089844   \n",
      "1   2017-02-01  19923.810547  20851.330078  19831.089844  20812.240234   \n",
      "2   2017-03-01  20957.289063  21169.109375  20412.800781  20663.220703   \n",
      "3   2017-04-01  20665.169922  21070.900391  20379.550781  20940.509766   \n",
      "4   2017-05-01  20962.730469  21112.320313  20553.449219  21008.650391   \n",
      "5   2017-06-01  21030.550781  21535.029297  20994.220703  21349.630859   \n",
      "6   2017-07-01  21392.300781  21929.800781  21279.300781  21891.119141   \n",
      "7   2017-08-01  21961.419922  22179.109375  21600.339844  21948.099609   \n",
      "8   2017-09-01  21981.769531  22419.509766  21709.630859  22405.089844   \n",
      "9   2017-10-01  22423.470703  23485.250000  22416.000000  23377.240234   \n",
      "10  2017-11-01  23442.900391  24327.820313  23242.750000  24272.349609   \n",
      "11  2017-12-01  24305.400391  24876.070313  23921.900391  24719.220703   \n",
      "\n",
      "       Adj Close      Volume  \n",
      "0   19864.089844  6482450000  \n",
      "1   20812.240234  6185580000  \n",
      "2   20663.220703  6941970000  \n",
      "3   20940.509766  5392630000  \n",
      "4   21008.650391  6613570000  \n",
      "5   21349.630859  7214590000  \n",
      "6   21891.119141  5569720000  \n",
      "7   21948.099609  6150060000  \n",
      "8   22405.089844  6342130000  \n",
      "9   23377.240234  7302910000  \n",
      "10  24272.349609  7335640000  \n",
      "11  24719.220703  6589890000  \n"
     ]
    }
   ],
   "source": [
    "print(dowjones_stocks)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Load **NFLX_daily_by_quarter.csv** into a DataFrame called `netflix_stocks_quarterly`. Then, quickly inspect the DataFrame using `print()`.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [],
   "source": [
    "netflix_stocks_quarterly = pd.read_csv('NFLX_daily_by_quarter.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "           Date        Open        High         Low       Close   Adj Close  \\\n",
      "0    2017-01-03  124.959999  128.190002  124.309998  127.489998  127.489998   \n",
      "1    2017-01-04  127.489998  130.169998  126.550003  129.410004  129.410004   \n",
      "2    2017-01-05  129.220001  132.750000  128.899994  131.809998  131.809998   \n",
      "3    2017-01-06  132.080002  133.880005  129.809998  131.070007  131.070007   \n",
      "4    2017-01-09  131.479996  131.990005  129.889999  130.949997  130.949997   \n",
      "5    2017-01-10  131.270004  132.220001  129.289993  129.889999  129.889999   \n",
      "6    2017-01-11  130.910004  131.500000  129.250000  130.500000  130.500000   \n",
      "7    2017-01-12  130.630005  130.850006  128.500000  129.179993  129.179993   \n",
      "8    2017-01-13  131.149994  133.929993  130.580002  133.699997  133.699997   \n",
      "9    2017-01-17  135.039993  135.399994  132.089996  132.889999  132.889999   \n",
      "10   2017-01-18  133.210007  133.649994  131.059998  133.259995  133.259995   \n",
      "11   2017-01-19  142.009995  143.460007  138.250000  138.410004  138.410004   \n",
      "12   2017-01-20  139.360001  140.789993  137.660004  138.600006  138.600006   \n",
      "13   2017-01-23  138.649994  139.490005  137.309998  137.389999  137.389999   \n",
      "14   2017-01-24  138.110001  140.929993  137.029999  140.110001  140.110001   \n",
      "15   2017-01-25  140.800003  141.389999  139.050003  139.520004  139.520004   \n",
      "16   2017-01-26  140.449997  141.210007  138.509995  138.960007  138.960007   \n",
      "17   2017-01-27  139.460007  142.490005  139.000000  142.449997  142.449997   \n",
      "18   2017-01-30  141.770004  141.970001  138.800003  141.220001  141.220001   \n",
      "19   2017-01-31  140.550003  141.830002  139.699997  140.710007  140.710007   \n",
      "20   2017-02-01  141.199997  142.410004  139.300003  140.779999  140.779999   \n",
      "21   2017-02-02  140.610001  141.039993  139.050003  139.199997  139.199997   \n",
      "22   2017-02-03  139.509995  140.639999  139.100006  140.250000  140.250000   \n",
      "23   2017-02-06  140.000000  141.000000  139.160004  140.970001  140.970001   \n",
      "24   2017-02-07  141.490005  144.279999  141.050003  144.000000  144.000000   \n",
      "25   2017-02-08  143.570007  145.070007  142.559998  144.740005  144.740005   \n",
      "26   2017-02-09  144.979996  145.089996  143.580002  144.139999  144.139999   \n",
      "27   2017-02-10  144.679993  145.300003  143.970001  144.820007  144.820007   \n",
      "28   2017-02-13  145.190002  145.949997  143.050003  143.199997  143.199997   \n",
      "29   2017-02-14  143.199997  144.110001  140.050003  140.820007  140.820007   \n",
      "..          ...         ...         ...         ...         ...         ...   \n",
      "221  2017-11-16  194.330002  197.699997  193.750000  195.509995  195.509995   \n",
      "222  2017-11-17  195.740005  195.949997  192.649994  193.199997  193.199997   \n",
      "223  2017-11-20  193.300003  194.320007  191.899994  194.100006  194.100006   \n",
      "224  2017-11-21  195.039993  197.520004  194.970001  196.229996  196.229996   \n",
      "225  2017-11-22  196.580002  196.750000  193.630005  196.320007  196.320007   \n",
      "226  2017-11-24  196.649994  196.899994  195.330002  195.750000  195.750000   \n",
      "227  2017-11-27  195.559998  195.850006  194.000000  195.050003  195.050003   \n",
      "228  2017-11-28  195.339996  199.679993  194.009995  199.179993  199.179993   \n",
      "229  2017-11-29  198.910004  199.029999  184.320007  188.149994  188.149994   \n",
      "230  2017-11-30  190.309998  190.860001  186.679993  187.580002  187.580002   \n",
      "231  2017-12-01  186.990005  189.800003  185.000000  186.820007  186.820007   \n",
      "232  2017-12-04  189.360001  189.720001  178.380005  184.039993  184.039993   \n",
      "233  2017-12-05  183.500000  188.139999  181.190002  184.210007  184.210007   \n",
      "234  2017-12-06  183.380005  186.479996  182.880005  185.300003  185.300003   \n",
      "235  2017-12-07  185.710007  187.339996  183.220001  185.199997  185.199997   \n",
      "236  2017-12-08  186.500000  189.419998  186.300003  188.539993  188.539993   \n",
      "237  2017-12-11  187.850006  189.419998  185.910004  186.220001  186.220001   \n",
      "238  2017-12-12  186.009995  187.850006  184.820007  185.729996  185.729996   \n",
      "239  2017-12-13  186.100006  188.690002  185.410004  187.860001  187.860001   \n",
      "240  2017-12-14  187.979996  192.639999  187.199997  189.559998  189.559998   \n",
      "241  2017-12-15  189.610001  191.429993  188.009995  190.119995  190.119995   \n",
      "242  2017-12-18  191.199997  191.649994  188.899994  190.419998  190.419998   \n",
      "243  2017-12-19  190.179993  190.300003  185.750000  187.020004  187.020004   \n",
      "244  2017-12-20  187.940002  189.110001  185.259995  188.820007  188.820007   \n",
      "245  2017-12-21  189.440002  190.949997  187.580002  188.619995  188.619995   \n",
      "246  2017-12-22  188.330002  190.949997  186.800003  189.940002  189.940002   \n",
      "247  2017-12-26  189.779999  189.940002  186.399994  187.759995  187.759995   \n",
      "248  2017-12-27  187.800003  188.100006  185.220001  186.240005  186.240005   \n",
      "249  2017-12-28  187.179993  194.490005  186.850006  192.710007  192.710007   \n",
      "250  2017-12-29  192.509995  193.949997  191.220001  191.960007  191.960007   \n",
      "\n",
      "       Volume Quarter  \n",
      "0     9437900      Q1  \n",
      "1     7843600      Q1  \n",
      "2    10185500      Q1  \n",
      "3    10657900      Q1  \n",
      "4     5766900      Q1  \n",
      "5     5985800      Q1  \n",
      "6     5615100      Q1  \n",
      "7     5388900      Q1  \n",
      "8    10515000      Q1  \n",
      "9    12183200      Q1  \n",
      "10   16168600      Q1  \n",
      "11   23203400      Q1  \n",
      "12    9497400      Q1  \n",
      "13    7433900      Q1  \n",
      "14    7754700      Q1  \n",
      "15    7238100      Q1  \n",
      "16    6038300      Q1  \n",
      "17    8323900      Q1  \n",
      "18    8122500      Q1  \n",
      "19    4411600      Q1  \n",
      "20    6033400      Q1  \n",
      "21    3462400      Q1  \n",
      "22    3512600      Q1  \n",
      "23    3552100      Q1  \n",
      "24    8573500      Q1  \n",
      "25    6887100      Q1  \n",
      "26    4555100      Q1  \n",
      "27    6171900      Q1  \n",
      "28    4790400      Q1  \n",
      "29    8355000      Q1  \n",
      "..        ...     ...  \n",
      "221   5678400      Q4  \n",
      "222   3906300      Q4  \n",
      "223   3827500      Q4  \n",
      "224   4787300      Q4  \n",
      "225   5895400      Q4  \n",
      "226   2160500      Q4  \n",
      "227   3210100      Q4  \n",
      "228   6981100      Q4  \n",
      "229  14202700      Q4  \n",
      "230   6630100      Q4  \n",
      "231   6219500      Q4  \n",
      "232   9069800      Q4  \n",
      "233   5783700      Q4  \n",
      "234   5490100      Q4  \n",
      "235   4659500      Q4  \n",
      "236   4987300      Q4  \n",
      "237   5298600      Q4  \n",
      "238   4265900      Q4  \n",
      "239   4710000      Q4  \n",
      "240   7792800      Q4  \n",
      "241   7285600      Q4  \n",
      "242   5011000      Q4  \n",
      "243   7033000      Q4  \n",
      "244   6545400      Q4  \n",
      "245   4729800      Q4  \n",
      "246   3878900      Q4  \n",
      "247   3045700      Q4  \n",
      "248   4002100      Q4  \n",
      "249  10107400      Q4  \n",
      "250   5187600      Q4  \n",
      "\n",
      "[251 rows x 8 columns]\n"
     ]
    }
   ],
   "source": [
    "print(netflix_stocks_quarterly)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's learn more about our data. The datasets are large and it may be easier to view the entire dataset locally on your computer. Open the CSV files directly from the folder you downloaded for this project.\n",
    " - `NFLX` is the stock ticker symbol for Netflix and `^DJI` is the stock ticker symbol for the Dow Jones industrial Average, which is why the CSV files are named accordingly\n",
    " - In the Yahoo Data, `Adj Close` is documented as adjusted close price adjusted for both dividends and splits.\n",
    " - You can learn more about why the Dow Jones Industrial Average is a industry reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp). \n",
    " \n",
    "Answer the following questions by inspecting the data in the **NFLX.csv**,**DJI.csv**, and **NFLX_daily_by_quarter.csv** in your computer."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What year is represented in the data? Look out for the latest and earliest date."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2017"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "+ Is the data represented by days, weeks, or months? \n",
    "+ In which ways are the files different? \n",
    "+ What's different about the columns for `netflix_stocks` versus `netflix_stocks_quarterly`?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "netflix_stocks represents data by months.  netflix_stocks_quarterly represents the data by day and quarter."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "netflix_stocks aggregates the data by months so it has fewer data points than netflix_stocks_quarterly "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The columns between the two data frames are the same except netflix_stocks_quarterly has one additional column for quarter."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 4\n",
    "\n",
    "Great! Now that we have spent sometime looking at the data, let's look at the column names of the DataFrame `netflix_stocks` using `.head()`. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Adj Close</th>\n",
       "      <th>Volume</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2017-01-01</td>\n",
       "      <td>124.959999</td>\n",
       "      <td>143.460007</td>\n",
       "      <td>124.309998</td>\n",
       "      <td>140.710007</td>\n",
       "      <td>140.710007</td>\n",
       "      <td>181772200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2017-02-01</td>\n",
       "      <td>141.199997</td>\n",
       "      <td>145.949997</td>\n",
       "      <td>139.050003</td>\n",
       "      <td>142.130005</td>\n",
       "      <td>142.130005</td>\n",
       "      <td>91432000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2017-03-01</td>\n",
       "      <td>142.839996</td>\n",
       "      <td>148.289993</td>\n",
       "      <td>138.259995</td>\n",
       "      <td>147.809998</td>\n",
       "      <td>147.809998</td>\n",
       "      <td>110692700</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2017-04-01</td>\n",
       "      <td>146.699997</td>\n",
       "      <td>153.520004</td>\n",
       "      <td>138.660004</td>\n",
       "      <td>152.199997</td>\n",
       "      <td>152.199997</td>\n",
       "      <td>149769200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2017-05-01</td>\n",
       "      <td>151.910004</td>\n",
       "      <td>164.750000</td>\n",
       "      <td>151.610001</td>\n",
       "      <td>163.070007</td>\n",
       "      <td>163.070007</td>\n",
       "      <td>116795800</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Date        Open        High         Low       Close   Adj Close  \\\n",
       "0  2017-01-01  124.959999  143.460007  124.309998  140.710007  140.710007   \n",
       "1  2017-02-01  141.199997  145.949997  139.050003  142.130005  142.130005   \n",
       "2  2017-03-01  142.839996  148.289993  138.259995  147.809998  147.809998   \n",
       "3  2017-04-01  146.699997  153.520004  138.660004  152.199997  152.199997   \n",
       "4  2017-05-01  151.910004  164.750000  151.610001  163.070007  163.070007   \n",
       "\n",
       "      Volume  \n",
       "0  181772200  \n",
       "1   91432000  \n",
       "2  110692700  \n",
       "3  149769200  \n",
       "4  116795800  "
      ]
     },
     "execution_count": 112,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "netflix_stocks.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What do you notice? The first two column names are one word each, and the only one that is not is `Adj Close`! \n",
    "\n",
    "The term `Adj Close` is a confusing term if you don't read the Yahoo Documentation. In Yahoo, `Adj Close` is documented as adjusted close price adjusted for both dividends and splits.\n",
    "\n",
    "This means this is the column with the true closing price, so these data are very important.\n",
    "\n",
    "Use Pandas to change the name of of the column to `Adj Close` to `Price` so that it is easier to work with the data. Remember to use `inplace=True`.\n",
    "\n",
    "Do this for the Dow Jones and Netflix Quarterly pandas dataframes as well.\n",
    "Hint: Use [`.rename()`](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html)).\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "metadata": {},
   "outputs": [],
   "source": [
    "netflix_stocks.rename(columns={'Adj Close': 'Price'}, inplace=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Run `netflix_stocks.head()` again to check your column name has changed."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Price</th>\n",
       "      <th>Volume</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2017-01-01</td>\n",
       "      <td>124.959999</td>\n",
       "      <td>143.460007</td>\n",
       "      <td>124.309998</td>\n",
       "      <td>140.710007</td>\n",
       "      <td>140.710007</td>\n",
       "      <td>181772200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2017-02-01</td>\n",
       "      <td>141.199997</td>\n",
       "      <td>145.949997</td>\n",
       "      <td>139.050003</td>\n",
       "      <td>142.130005</td>\n",
       "      <td>142.130005</td>\n",
       "      <td>91432000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2017-03-01</td>\n",
       "      <td>142.839996</td>\n",
       "      <td>148.289993</td>\n",
       "      <td>138.259995</td>\n",
       "      <td>147.809998</td>\n",
       "      <td>147.809998</td>\n",
       "      <td>110692700</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2017-04-01</td>\n",
       "      <td>146.699997</td>\n",
       "      <td>153.520004</td>\n",
       "      <td>138.660004</td>\n",
       "      <td>152.199997</td>\n",
       "      <td>152.199997</td>\n",
       "      <td>149769200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2017-05-01</td>\n",
       "      <td>151.910004</td>\n",
       "      <td>164.750000</td>\n",
       "      <td>151.610001</td>\n",
       "      <td>163.070007</td>\n",
       "      <td>163.070007</td>\n",
       "      <td>116795800</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Date        Open        High         Low       Close       Price  \\\n",
       "0  2017-01-01  124.959999  143.460007  124.309998  140.710007  140.710007   \n",
       "1  2017-02-01  141.199997  145.949997  139.050003  142.130005  142.130005   \n",
       "2  2017-03-01  142.839996  148.289993  138.259995  147.809998  147.809998   \n",
       "3  2017-04-01  146.699997  153.520004  138.660004  152.199997  152.199997   \n",
       "4  2017-05-01  151.910004  164.750000  151.610001  163.070007  163.070007   \n",
       "\n",
       "      Volume  \n",
       "0  181772200  \n",
       "1   91432000  \n",
       "2  110692700  \n",
       "3  149769200  \n",
       "4  116795800  "
      ]
     },
     "execution_count": 114,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "netflix_stocks.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {},
   "outputs": [],
   "source": [
    "netflix_stocks_quarterly.rename(columns={'Adj Close': 'Price'}, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {},
   "outputs": [],
   "source": [
    "dowjones_stocks.rename(columns={'Adj Close': 'Price'}, inplace=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Call `.head()` on the DataFrame `dowjones_stocks` and `netflix_stocks_quarterly`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Price</th>\n",
       "      <th>Volume</th>\n",
       "      <th>Quarter</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2017-01-03</td>\n",
       "      <td>124.959999</td>\n",
       "      <td>128.190002</td>\n",
       "      <td>124.309998</td>\n",
       "      <td>127.489998</td>\n",
       "      <td>127.489998</td>\n",
       "      <td>9437900</td>\n",
       "      <td>Q1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2017-01-04</td>\n",
       "      <td>127.489998</td>\n",
       "      <td>130.169998</td>\n",
       "      <td>126.550003</td>\n",
       "      <td>129.410004</td>\n",
       "      <td>129.410004</td>\n",
       "      <td>7843600</td>\n",
       "      <td>Q1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2017-01-05</td>\n",
       "      <td>129.220001</td>\n",
       "      <td>132.750000</td>\n",
       "      <td>128.899994</td>\n",
       "      <td>131.809998</td>\n",
       "      <td>131.809998</td>\n",
       "      <td>10185500</td>\n",
       "      <td>Q1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2017-01-06</td>\n",
       "      <td>132.080002</td>\n",
       "      <td>133.880005</td>\n",
       "      <td>129.809998</td>\n",
       "      <td>131.070007</td>\n",
       "      <td>131.070007</td>\n",
       "      <td>10657900</td>\n",
       "      <td>Q1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2017-01-09</td>\n",
       "      <td>131.479996</td>\n",
       "      <td>131.990005</td>\n",
       "      <td>129.889999</td>\n",
       "      <td>130.949997</td>\n",
       "      <td>130.949997</td>\n",
       "      <td>5766900</td>\n",
       "      <td>Q1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Date        Open        High         Low       Close       Price  \\\n",
       "0  2017-01-03  124.959999  128.190002  124.309998  127.489998  127.489998   \n",
       "1  2017-01-04  127.489998  130.169998  126.550003  129.410004  129.410004   \n",
       "2  2017-01-05  129.220001  132.750000  128.899994  131.809998  131.809998   \n",
       "3  2017-01-06  132.080002  133.880005  129.809998  131.070007  131.070007   \n",
       "4  2017-01-09  131.479996  131.990005  129.889999  130.949997  130.949997   \n",
       "\n",
       "     Volume Quarter  \n",
       "0   9437900      Q1  \n",
       "1   7843600      Q1  \n",
       "2  10185500      Q1  \n",
       "3  10657900      Q1  \n",
       "4   5766900      Q1  "
      ]
     },
     "execution_count": 117,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "netflix_stocks_quarterly.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Price</th>\n",
       "      <th>Volume</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2017-01-01</td>\n",
       "      <td>19872.859375</td>\n",
       "      <td>20125.580078</td>\n",
       "      <td>19677.939453</td>\n",
       "      <td>19864.089844</td>\n",
       "      <td>19864.089844</td>\n",
       "      <td>6482450000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2017-02-01</td>\n",
       "      <td>19923.810547</td>\n",
       "      <td>20851.330078</td>\n",
       "      <td>19831.089844</td>\n",
       "      <td>20812.240234</td>\n",
       "      <td>20812.240234</td>\n",
       "      <td>6185580000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2017-03-01</td>\n",
       "      <td>20957.289063</td>\n",
       "      <td>21169.109375</td>\n",
       "      <td>20412.800781</td>\n",
       "      <td>20663.220703</td>\n",
       "      <td>20663.220703</td>\n",
       "      <td>6941970000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2017-04-01</td>\n",
       "      <td>20665.169922</td>\n",
       "      <td>21070.900391</td>\n",
       "      <td>20379.550781</td>\n",
       "      <td>20940.509766</td>\n",
       "      <td>20940.509766</td>\n",
       "      <td>5392630000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2017-05-01</td>\n",
       "      <td>20962.730469</td>\n",
       "      <td>21112.320313</td>\n",
       "      <td>20553.449219</td>\n",
       "      <td>21008.650391</td>\n",
       "      <td>21008.650391</td>\n",
       "      <td>6613570000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Date          Open          High           Low         Close  \\\n",
       "0  2017-01-01  19872.859375  20125.580078  19677.939453  19864.089844   \n",
       "1  2017-02-01  19923.810547  20851.330078  19831.089844  20812.240234   \n",
       "2  2017-03-01  20957.289063  21169.109375  20412.800781  20663.220703   \n",
       "3  2017-04-01  20665.169922  21070.900391  20379.550781  20940.509766   \n",
       "4  2017-05-01  20962.730469  21112.320313  20553.449219  21008.650391   \n",
       "\n",
       "          Price      Volume  \n",
       "0  19864.089844  6482450000  \n",
       "1  20812.240234  6185580000  \n",
       "2  20663.220703  6941970000  \n",
       "3  20940.509766  5392630000  \n",
       "4  21008.650391  6613570000  "
      ]
     },
     "execution_count": 118,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dowjones_stocks.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 5\n",
    "\n",
    "In this step, we will be visualizing the Netflix quarterly data! \n",
    "\n",
    "We want to get an understanding of the distribution of the Netflix quarterly stock prices for 2017. Specifically, we want to see in which quarter stock prices flucutated the most. We can accomplish this using a violin plot with four violins, one for each business quarter!\n",
    "\n",
    "\n",
    "1. Start by creating a variable `ax` and setting it equal to `sns.violinplot()`. This will instantiate a figure and give us access to the axes through the variable name `ax`.\n",
    "2. Use `sns.violinplot()` and pass in the following arguments:\n",
    "+ The `Quarter` column as the `x` values\n",
    "+ The `Price` column as your `y` values\n",
    "+ The `netflix_stocks_quarterly` dataframe as your `data`\n",
    "3. Improve the readability of the chart by adding a title of the plot. Add `\"Distribution of 2017 Netflix Stock Prices by Quarter\"` by using `ax.set_title()`\n",
    "4. Change your `ylabel` to \"Closing Stock Price\"\n",
    "5. Change your `xlabel` to \"Business Quarters in 2017\"\n",
    "6. Be sure to show your plot!\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "ax = sns.violinplot(data=netflix_stocks_quarterly, x=\"Quarter\", y=\"Price\")\n",
    "ax.set_title(\"Distribution of 2017 Netflix Stock Prices by Quarter\")\n",
    "ax.set_ylabel(\"Closing Stock Price\")\n",
    "ax.set_xlabel(\"Business Quarters in 2017\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Figure size 432x288 with 0 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.savefig(\"2017PricesbyQuarter.png\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Graph Literacy\n",
    "- What are your first impressions looking at the visualized data?\n",
    "\n",
    "- In what range(s) did most of the prices fall throughout the year?\n",
    "\n",
    "- What were the highest and lowest prices? "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 6\n",
    "\n",
    "Next, we will chart the performance of the earnings per share (EPS) by graphing the estimate Yahoo projected for the Quarter compared to the actual earnings for that quarters. We will accomplish this using a scatter chart. \n",
    "\n",
    "1. Plot the actual EPS by using `x_positions` and `earnings_actual` with the `plt.scatter()` function. Assign `red` as the color.\n",
    "2. Plot the actual EPS by using `x_positions` and `earnings_estimate` with the `plt.scatter()` function. Assign `blue` as the color\n",
    "\n",
    "3. Often, estimates and actual EPS are the same. To account for this, be sure to set your transparency  `alpha=0.5` to allow for visibility pf overlapping datapoint.\n",
    "4. Add a legend by using `plt.legend()` and passing in a list with two strings `[\"Actual\", \"Estimate\"]`\n",
    "\n",
    "5. Change the `x_ticks` label to reflect each quarter by using `plt.xticks(x_positions, chart_labels)`\n",
    "6. Assing \"`\"Earnings Per Share in Cents\"` as the title of your plot.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "x_positions = [1, 2, 3, 4]\n",
    "chart_labels = [\"1Q2017\",\"2Q2017\",\"3Q2017\",\"4Q2017\"]\n",
    "earnings_actual =[.4, .15,.29,.41]\n",
    "earnings_estimate = [.37,.15,.32,.41 ]\n",
    "plt.scatter(x_positions,earnings_actual, color=\"red\", alpha=0.5)\n",
    "plt.scatter(x_positions,earnings_estimate, color=\"blue\", alpha=0.5)\n",
    "plt.legend([\"Actuals\",\"Estimate\"])\n",
    "plt.xticks(x_positions, chart_labels)\n",
    "plt.title(\"Earnings Per Share in Cents\")\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Figure size 432x288 with 0 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.savefig(\"EarningPerShare.png\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "## Graph Literacy\n",
    "\n",
    "+ What do the purple dots tell us about the actual and estimate earnings per share in this graph? Hint: In color theory red and blue mix to make purple.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 7"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Next, we will visualize the earnings and revenue reported by Netflix by mapping two bars side-by-side. We have visualized a similar chart in the second Matplotlib lesson [Exercise 4](https://www.codecademy.com/courses/learn-matplotlib/lessons/matplotlib-ii/exercises/side-by-side-bars).\n",
    "\n",
    "As you may recall, plotting side-by-side bars in Matplotlib requires computing the width of each bar before hand. We have pasted the starter code for that exercise below. \n",
    "\n",
    "1. Fill in the `n`, `t`, `d`, `w` values for the revenue bars\n",
    "2. Plot the revenue bars by calling `plt.bar()` with the newly computed `x_values` and the `revenue_by_quarter` data\n",
    "3. Fill in the `n`, `t`, `d`, `w` values for the earnings bars\n",
    "4. Plot the revenue bars by calling `plt.bar()` with the newly computed `x_values` and the `earnings_by_quarter` data\n",
    "5. Create a legend for your bar chart with the `labels` provided\n",
    "6. Add a descriptive title for your chart with `plt.title()`\n",
    "7. Add labels to each quarter by assigning the position of the ticks through the code provided. Hint:  `plt.xticks(middle_x, quarter_labels)`\n",
    "8. Be sure to show your plot!\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 145,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# The metrics below are in billions of dollars\n",
    "revenue_by_quarter = [2.79, 2.98,3.29,3.7]\n",
    "earnings_by_quarter = [.0656,.12959,.18552,.29012]\n",
    "quarter_labels = [\"2Q2017\",\"3Q2017\",\"4Q2017\", \"1Q2018\"]\n",
    "\n",
    "# Revenue\n",
    "n = 1  # This is our first dataset (out of 2)\n",
    "t = 2 # Number of dataset\n",
    "d = 4 # Number of sets of bars\n",
    "w = 0.8 # Width of each bar\n",
    "bars1_x = [t*element + w*n for element\n",
    "             in range(d)]\n",
    "plt.bar(bars1_x,revenue_by_quarter)\n",
    "\n",
    "# Earnings\n",
    "n = 2  # This is our second dataset (out of 2)\n",
    "t = 2 # Number of dataset\n",
    "d = 4 # Number of sets of bars\n",
    "w = 0.8 # Width of each bar\n",
    "bars2_x = [t*element + w*n for element\n",
    "             in range(d)]\n",
    "plt.bar(bars2_x,earnings_by_quarter)\n",
    "\n",
    "middle_x = [ (a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]\n",
    "labels = [\"Revenue\", \"Earnings\"]\n",
    "plt.legend(labels)\n",
    "plt.title(\"Revenue vs. Earnings in Billions\")\n",
    "plt.xticks(middle_x, quarter_labels)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Graph Literacy\n",
    "What are your first impressions looking at the visualized data?\n",
    "\n",
    "- Does Revenue follow a trend?\n",
    "- Do Earnings follow a trend?\n",
    "- Roughly, what percentage of the revenue constitutes earnings?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Figure size 432x288 with 0 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.savefig(\"RevenuevsEarnings.png\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 8\n",
    "\n",
    "In this last step, we will compare Netflix stock to the Dow Jones Industrial Average in 2017. We will accomplish this by plotting two line charts side by side in one figure. \n",
    "\n",
    "Since `Price` which is the most relevant data is in the Y axis, let's map our subplots to align vertically side by side.\n",
    "- We have set up the code for you on line 1 in the cell below. Complete the figure by passing the following arguments to `plt.subplots()` for the first plot, and tweaking the third argument for the second plot\n",
    "    - `1`-- the number of rows for the subplots\n",
    "    - `2` -- the number of columns for the subplots\n",
    "    - `1` -- the subplot you are modifying\n",
    "\n",
    "- Chart the Netflix Stock Prices in the left-hand subplot. Using your data frame, access the `Date` and `Price` charts as the x and y axes respectively. Hint: (`netflix_stocks['Date'], netflix_stocks['Price']`)\n",
    "- Assign \"Netflix\" as a title to this subplot. Hint: `ax1.set_title()`\n",
    "- For each subplot, `set_xlabel` to `\"Date\"` and `set_ylabel` to `\"Stock Price\"`\n",
    "- Chart the Dow Jones Stock Prices in the left-hand subplot. Using your data frame, access the `Date` and `Price` charts as the x and y axes respectively. Hint: (`dowjones_stocks['Date'], dowjones_stocks['Price']`)\n",
    "- Assign \"Dow Jones\" as a title to this subplot. Hint: `plt.set_title()`\n",
    "- There is some crowding in the Y axis labels, add some space by calling `plt.subplots_adjust(wspace=.5)`\n",
    "- Be sure to `.show()` your plots.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Note from student -- Please note:  Following these directions produced charts with unreadable x axis labels.  Therefore, varied from the instructions to make the charts more readable."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 146,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1080x144 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1080x144 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Left plot Netflix\n",
    "fig = plt.figure(figsize=(15, 2))\n",
    "dateticks = [\"JAN\", \"FEB\", \"MAR\", \"APR\", \"MAY\", \"JUN\", \"JUL\", \"AUG\", \"SEP\", \"OCT\", \"NOV\", \"DEC\"]\n",
    "ax1 = plt.subplot(1, 2, 1)\n",
    "plt.plot(netflix_stocks['Date'], netflix_stocks['Price'])\n",
    "plt.subplots_adjust(wspace = .5)\n",
    "ax1.set_title(\"Netflix 2017\")\n",
    "ax1.set_xlabel(\"Date\")\n",
    "ax1.set_ylabel(\"Stock Price\")\n",
    "ax1.set_xticklabels(dateticks)\n",
    "# Right plot Dow Jones\n",
    "fig = plt.figure(figsize=(15, 2)) \n",
    "dateticks = [\"JAN\", \"FEB\", \"MAR\", \"APR\", \"MAY\", \"JUN\", \"JUL\", \"AUG\", \"SEP\", \"OCT\", \"NOV\", \"DEC\"]\n",
    "ax2 = plt.subplot(1, 2, 2)\n",
    "plt.plot(dowjones_stocks['Date'], dowjones_stocks['Price'])\n",
    "plt.subplots_adjust(wspace = .5, bottom = .3)\n",
    "ax2.set_title(\"Dow Jones 2017\")\n",
    "ax2.set_xlabel(\"Date\")\n",
    "ax2.set_ylabel(\"Stock Price\")\n",
    "ax2.set_xticklabels(dateticks)\n",
    "\n",
    "\n",
    "\n",
    "              \n",
    "plt.show()\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- How did Netflix perform relative to Dow Jones Industrial Average in 2017?\n",
    "- Which was more volatile?\n",
    "- How do the prices of the stocks compare?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 144,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Figure size 432x288 with 0 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.savefig(\"NetflixvsDowJones.png\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 9\n",
    "\n",
    "It's time to make your presentation! Save each of your visualizations as a png file with `plt.savefig(\"filename.png\")`.\n",
    "\n",
    "As you prepare your slides, think about the answers to the graph literacy questions. Embed your observations in the narrative of your slideshow!\n",
    "\n",
    "Remember that your slideshow must include:\n",
    "- A title slide\n",
    "- A list of your visualizations and your role in their creation for the \"Stock Profile\" team\n",
    "- A visualization of the distribution of the stock prices for Netflix in 2017\n",
    "- A visualization and a summary of Netflix stock and revenue for the past four quarters and a summary\n",
    "- A visualization and a brief summary of their earned versus actual earnings per share\n",
    "- A visualization of Netflix stock against the Dow Jones stock (to get a sense of the market) in 2017\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
