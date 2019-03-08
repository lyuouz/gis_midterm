#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pysal as ps
import geopandas as gpd
import matplotlib.pyplot as plt
plt.style.use(['seaborn', 'fivethirtyeight'])


# In[3]:


cali_health = gpd.read_file('/Users/zhanglvou/Desktop/GoMailman/spring_2019/gis/Midterm_Materials_Spring19_AdvGIS/gis_midterm/data/cali_health_data.shp')
cali_health.head()


# In[4]:


cali_health.plot();


# In[5]:


plt.subplots(2, 3)


# In[6]:


fig, ax = plt.subplots(3, 2, figsize=(17, 22))
# defining map property details
title_size = 23
legend_kwds = {'loc': 3, 'fontsize': 10,
               'title': 'Quantiles',
               'title_fontsize': 12.5}
cali_health.plot(column='prcnt_f_', legend_kwds=legend_kwds, ax=ax[0][0],
         legend=True, cmap='Greens', scheme='quantiles', k=5,
         edgecolor='k', lw=0.7)
ax[0][0].set_title('% Poor and Fair Health in California by County', fontsize=title_size)
cali_health.plot(column='prcnt_b', legend_kwds=legend_kwds, ax=ax[0][1],
         legend=True, cmap='Greens', scheme='quantiles', k=5,
         edgecolor='k', lw=0.7)
ax[0][1].set_title('% Obesity', fontsize=title_size)
cali_health.plot(column='prcnt_p_', legend_kwds=legend_kwds, ax=ax[1][0],
         legend=True, cmap='Greens', scheme='quantiles', k=5,
         edgecolor='k', lw=0.7)
ax[1][0].set_title('% Physically Inactive', fontsize=title_size)
cali_health.plot(column='prcnt_w_', legend_kwds=legend_kwds, ax=ax[1][1],
         legend=True, cmap='Greens', scheme='quantiles', k=5,
         edgecolor='k', lw=0.7)
ax[1][1].set_title('% With Access to Exercise Opportunities', fontsize=title_size)
cali_health.plot(column='prcnt_x_', legend_kwds=legend_kwds, ax=ax[2][0],
         legend=True, cmap='Greens', scheme='quantiles', k=5,
         edgecolor='k', lw=0.7)
ax[2][0].set_title('% Excess Drinking', fontsize=title_size)
cali_health.plot(column='prcnt_s', legend_kwds=legend_kwds, ax=ax[2][1],
         legend=True, cmap='Greens', scheme='quantiles', k=5,
         edgecolor='k', lw=0.7)
ax[2][1].set_title('% Adult Smoking', fontsize=title_size)
ax[2][1].annotate('Data source: 2018 County Health Rankings California Data', xy = (0, -0.3), xycoords="axes fraction", fontsize=15)
# add title
fig_title = 'Rank Measures Data by County in California'
plt.suptitle(fig_title, fontsize=28);
plt.tight_layout(rect=[0, 0, 1, 0.95])


# In[ ]:




