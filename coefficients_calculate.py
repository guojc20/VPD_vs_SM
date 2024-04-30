{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "19a68cbd-041e-47a3-b39a-f15590ba523d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "from scipy.stats import pearsonr\n",
    "\n",
    "data = pd.read_csv('xxxx.csv')    #### input .csv file\n",
    "data = data.rename(columns={'GPP.gross': 'GPP', 'ET.gross': 'ET', 'SWC_1_1_1': 'SWC'})\n",
    "df = data[['GPP', 'ET', 'VPD', 'SWC']]\n",
    "\n",
    "#### data control\n",
    "df = df.replace(0, pd.NA)\n",
    "df = df.dropna()\n",
    "\n",
    "#### Grouping data based on the percentage of SWC\n",
    "swc_percentiles = np.percentile(df['SWC'], np.linspace(0, 100, 11))\n",
    "df['SWC_percentile'] = pd.cut(df['SWC'], bins=swc_percentiles, labels=False, include_lowest=True)\n",
    "\n",
    "#### calulate coefficients between dryland fluxes and VPD/SM at each SM percentile\n",
    "pearsonr_swctype = {}\n",
    "for percent in range(10):\n",
    "    subset = df[df['SWC_percentile'] == percent]\n",
    "    pearsonr_swctype[percent] = {\n",
    "        'SWC percentile': (percent+1)*10,\n",
    "        'GPP_SWC': pearsonr(subset['GPP'], subset['SWC'])[0],\n",
    "        'ET_SWC': pearsonr(subset['ET'], subset['SWC'])[0],\n",
    "        'GPP_VPD': pearsonr(subset['GPP'], subset['VPD'])[0],\n",
    "        'ET_VPD': pearsonr(subset['ET'], subset['VPD'])[0]\n",
    "    }\n",
    "pearsonr_results_swctype = pd.DataFrame(pearsonr_swctype)\n",
    "\n",
    "print(pearsonr_results_swctype)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
