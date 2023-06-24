#dictionary (forest of 3 trees:)
families={
    'ram':
           {'radhi' :{'sham','chikki'}, 'mahi' :{'anvi'}},
    'mani':
           {'niki':{'pinky'}, 'wendy':{'dg'}, 'eg' :{'vinny'}},
    'siri':
          {'geet':'ali', 'sri' :'anisa'}
    }
for parent,children in families.items():
    print(f" {parent} has {len(children)} kid(s):")
    print(f"{' , and '.join([str(child) for child in [*children]])}")
