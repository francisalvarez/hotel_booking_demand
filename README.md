# Data
The data was downloaded from Kaggle.
https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand?phase=FinishSSORegistration&returnUrl=%2Fdatasets%2Fjessemostipak%2Fhotel-booking-demand%2Fversions%2F1%3Fresource%3Ddownload&SSORegistrationToken=CfDJ8GXdT74sZy9Iv4qC0qaf2Rf61U5cghMVcrIzVYejlgulhNkpQt-H_4S2JkygYL_VUoIwNsbzqwsZf-1V14Z_PmnTsyrWTf1Mu8_QfqF707zxNzsrt-aREOAfkQENnbL4SWFvYixqsWMdN6XIfbjE4tOOm1-wQATX-ycfWmAJ49IIHxzZfY8TQ1DYZPlg6xBMZ6HiGG3olWZD_XadA0TwZSa4yQ6yY4jJXBBb5DneFZUPNY6YGeFET1vAyPHZjuIvdUpjsqXE4CZdHHh0hA8rmex3XjkAvKaGW2gqse60qALh2jY7ry9HbfcuFSXEaw50t9wIgy1PFZunrKp5KL4gjmj-E-MT7FE&DisplayName=Francis+Alvarez

# Goals
- [ ] Logistic Regression - Predict Cancellation

# Reference Material

## Logistic Regression Inspiration
Applied Logistic Regression - 3E - Hosmer et al

Chapter 4.2 Purposeful Selection of Covariates


### Step 1
Step 1: Purposeful selection begins with a careful univariable analysis of each independent variable. **For categorical
variables we suggest doing this via a standard contingency table analysis of the outcome (y = 0, 1) versus the k levels
of the independent variable.** The usual likelihood ratio chi-square test with k − 1 degrees of freedom is exactly equal
to the value of the likelihood ratio test for the significance of the coefficients for the k − 1 design variables in a
univariable logistic regression model that contains that single independent variable. Since the Pearson chi-square test
is asymptotically equivalent to the likelihood ratio chi-square test, it may also be used. In addition to the overall
test, it is a good idea, for those variables exhibiting at least a moderate level of association, to estimate the 
individual odds ratios (along with confidence limits) using one of the levels as the reference group.

Particular attention should be paid to any contingency table with a zero (frequency) cell, since in that situation, 
most standard logistic regression software packages will fail to converge and produce a point estimate for one of the 
odds ratios of either zero or infinity. An intermediate strategy for dealing with this problem is to collapse categories
of the independent variable in some sensible fashion to eliminate the zero cell. If the covariate with the zero cell 
turns out to be statistically significant, we can revisit the problem at a later stage using one of the special programs
discussed in Section 10.3. Fortunately, the zero cell problem does not occur too frequently.

For continuous variables, the best univariable analysis involves fitting a univariable logistic regression model to obtain the estimated coefficient, the estimated standard error, the likelihood ratio test for the significance of the coefficient, and the univariable Wald statistic. An alternative analysis, which is nearly equivalent at the univariable level and that may be preferred in an applied setting, is based on the two-sample t-test. Descriptive statistics available from this analysis generally include group means, standard devia- tions, the t statistic, and its p-value. The similarity of this approach to the logistic regression analysis follows from the fact that the univariable linear discriminant function estimate of the logistic regression coefficient is

<insert t test equation>

and that the linear discriminant function and the maximum likelihood esti- mate of the logistic regression coefficient are usually quite close when the independent variable is approximately normally distributed within each of the outcome groups, y = 0, 1, [see Halpern et al. (1971)]. Thus, the univariable analysis based on the t-test can be used to determine whether the variable should be included in the model since the p-value should be of the same order of magnitude as that of the Wald statistic, Score test, or likelihood ratio test from logistic regression.
Through the use of these univariable analyses we identify, as candidates for a first multivariable model, any variable whose univariable test has a p-value less than 0.25 along with all variables of known clinical importance.
Our recommendation for using a significance level as high as 0.20 or 0.25 as a screening criterion for initial variable selection is based on the work by Bendel and Afifi (1977) on linear regression and on the work by Mickey and Greenland (1989) on logistic regression. These authors show that use of a more traditional level (such as 0.05) often fails to identify variables known to be important. Use of the higher level has the disadvantage of including variables that are of questionable importance at this initial stage of model development. For this reason, it is important to review all variables added to a model critically before a decision is reached regarding the final model.

### Step 2
Step 2: Fit the multivariable model containing all covariates identified for inclu- sion at Step 1. Following the fit of this model, we assess the importance of each covariate using the p-value of its Wald statistic. Variables that do not contribute, at traditional levels of statistical significance, should be eliminated and a new model fit. The new, smaller, model should be compared to the old, larger, model using the partial likelihood ratio test. This is especially impor- tant if more than one term has been removed from the model, which is always the case when a categorical variable with more than two levels has been included using two or more design variables that appear to be not significant. Also, one must pay attention to make sure that the samples used to fit the larger and smaller models are the same. This becomes an issue when there are missing data. We discuss strategies for handling missing data in Section 10.4.

### Step 3
Step 3: Following the fit of the smaller, reduced model we compare the values of the estimated coefficients in the smaller model to their respective values from the larger model. In particular, we should be concerned about any variable whose coefficient has changed markedly in magnitude [e.g., having a value of βˆ > 20%, see equation (3.9)]. This indicates that one or more of the excluded variables are important in the sense of providing a needed adjustment of the effect of the variables that remained in the model. Such variable(s) should be added back into the model. This process of deleting, refitting, and verifying continues, cycling through Step 2 and Step 3, until it appears that all of the important variables are included in the model and those excluded are clinically and/or statistically unimportant. In this process we recommend that one should proceed slowly by deleting only a few covariates at a time.

### Step 4
Step 4: Add each variable not selected in Step 1 to the model obtained at the conclusion of cycling through Step 2 and Step 3, one at a time, and check its significance either by the Wald statistic p-value or the partial likelihood ratio test, if it is a categorical variable with more than two levels. This step is vital for identifying variables that, by themselves, are not significantly related to the outcome but make an important contribution in the presence of other variables. We refer to the model at the end of Step 4 as the preliminary main effects model.

### Step 5
Step 5: Once we have obtained a model that we feel contains the essential variables, we examine more closely the variables in the model. The question of the appropriate categories for categorical variables should have been addressed during the univariable analysis in Step 1. For each continuous variable in this model we must check the assumption that the logit increases/decreases linearly as a function of the covariate. There are a number of techniques and methods to do this and we discuss them in Section 4.2.1. We refer to the model at the end of Step 5 as the main effects model.

### Step 6
Step 6: Once we have the main effects model, we check for interactions among the variables in the model. In any model, as discussed and illustrated with examples in Section 3.5, an interaction between two variables implies that the effect of each variable is not constant over levels of the other variable. As noted in Section 3.5, the final decision as to whether an interaction term should be included in a model should be based on statistical as well as practical considerations. Any interaction term in the model must make sense from a clinical perspective.
We address the clinical plausibility issue by creating a list of possible pairs of variables in the model that have some realistic possibility of interacting with each other. The interaction variables are created as the arithmetic prod- uct of the pairs of main effect variables. This can result in more than one interaction term. For example, the interaction of two categorical variables, each with three levels (i.e., two dummy variables), generates four interaction variables. We add the interactions, one at a time, to the main effects model from Step 5. (This may involve adding more than one term at a time to the
model.) We then assess the statistical significance of the interaction using a likelihood ratio test. Unlike main effects where we consider adjustment as well as significance, we only consider the statistical significance of interac- tions and as such, they must contribute to the model at traditional levels, such as 5% or even 1%. Inclusion of an interaction term in the model that is not significant typically just increases the estimated standard errors without much change in the point estimates of effect.
Following the univariable analysis of the interaction terms we add each interaction that was significant to the model at the end of Step 5. We then follow Step 2 to simplify the model, considering only the removal of the interaction terms, not any main effects. At this point we view the main effect terms as being “locked” and they cannot be removed from the model. One implication of “locking the main effects” is that we do not consider statistical adjustment, βˆ%, when winnowing insignificant interactions.
We refer to the model at the conclusion of Step 6 as the preliminary final model.

### Step 7
Step 7: Before any model becomes the final model we must assess its adequacy and check its fit. We discuss these methods in Chapter 5. Note that regardless of what method is used to obtain a multivariable statistical model, purposeful selection or any of the other methods discussed in this chapter, one must perform Step 7 before using the fitted model for inferential purposes.
