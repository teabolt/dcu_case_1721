# crosstab of pupils of ages in districts

age_categories = c(14, 15, 16, 17)
north_ages = c(.05, .1, .05, .1)
centre_ages = c(.1, .15, .05, .05)
south_ages = c(.15, .1, .05, .05)

district_ages = north_ages + centre_ages + south_ages
sum(district_ages)

# (i)

age15 = district_ages[2]
districtcentre = sum(centre_ages)
age15_districtcentre = (centre_ages[2])/districtcentre # NOT age15*distrinctcentre/distrinctcentre
age15_and_districtcentre = centre_ages[2] # NOT age15*districtcentre
age15_or_districtcentre = age15 + districtcentre - age15_and_districtcentre

# (ii)
m_age = sum(district_ages*age_categories)
v_age = sum(district_ages*(age_categories-m_age)^2)