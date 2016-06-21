#衰变模型

##简介
###本次作业选择课后习题1.4
####Consider a radioactive decay problem involving two types of nuclei,A and B,with populations N<sub>A</sub>(t) and N<sub>B</sub>(t).Suppose that type A nuclei decay to form type B nuclei,which then also decay,according to the differential equations 
<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cfrac%7B%24dN_A%24%7D%7Bdt%7D%3D-%5Cfrac%7B%24N_A%24%7D%7B%24%5Ctau%20_A%24%7D" style="border:none;" />

<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cfrac%7B%24dN_B%24%7D%7Bdt%7D%3D%5Cfrac%7B%24N_A%24%7D%7B%24%5Ctau%20_A%24%7D-%5Cfrac%7B%24N_B%24%7D%7B%24%5Ctau%20_B%24%7D" style="border:none;" />

####where<img src="http://chart.googleapis.com/chart?cht=tx&chl=%24%5Ctau%20_A%24" style="border:none;" />and <img src="http://chart.googleapis.com/chart?cht=tx&chl=%24%5Ctau%20_B%24" style="border:none;" /> are the decay time constants for each type of nucleis.Use the Euler method to solve these coupled equations for N<sub>A</sub>(t) and N<sub>B</sub>(t) as functions of time.This priblem can also be solved exactly,as was the case with our orginal nuclear decay problem (1.1).

##正文
我们的目标是获得N<sub>A</sub>(t)关于t的函数关系式。
对N<sub>A</sub>(t)进行泰勒展开有：

<img src="http://chart.googleapis.com/chart?cht=tx&chl=N_A(%5CDelta%20t)%3DN_A(0)%2B%5Cfrac%7B%24dN_A%24%7D%7Bdt%7D%5CDelta%20t%2B%5Cfrac%7B1%7D%7B2%7D%5Cfrac%7Bd%5E%7B2%7DN_A%7D%7Bdt%5E%7B2%7D%7D(%5CDelta%20t)%5E%7B2%7D%2B......" style="border:none;" />

当<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5CDelta%20t" style="border:none;" />趋近于0时，则忽略二次项及其之后的项就能有较好的近似。即：

<img src="http://chart.googleapis.com/chart?cht=tx&chl=N_A(%5CDelta%20t)%5Capprox%20N_A(0)%2B%5Cfrac%7BdN_A%7D%7Bdt%7D%5CDelta%20t" style="border:none;" />

通过微分定义公式可以得到同样的结果，即：

<img src="http://chart.googleapis.com/chart?cht=tx&chl=%5Cfrac%7BdN_A%7D%7Bdt%7D%5Cequiv%20%5Clim_%7B%5CDelta%20t%5Cto%5C0%7D%5Cfrac%7BN_A(t%2B%5CDelta%20t)-N_A(t)%7D%7B%5CDelta%20t%7D%5Capprox%20%5Cfrac%7BN_A(t%2B%5CDelta%20t)-N_A(t)%7D%7B%5CDelta%20t%7D" style="border:none;" />

将衰变规律代入上式可得：


#未完QAQ
