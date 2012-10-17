from races.models import Race, Result, Racer
import csv


def process_csv(filename):
    result_csv = csv.reader(open(filename))
    results = []
    for result in result_csv:
        results.append(record_result(result))
    return results


def record_result(result):
    r_dict = {'position': '', 'number': '', 'name': '', 'time': '', 'award': ''}
    r_dict['position'] = result[0]
    r_dict['number'] = int(result[1])
    r_dict['name'] = result[2]
    r_dict['time'] = result[3]
    r_dict['award'] = result[4]
    return r_dict


def process_results(race, results):
    for result in results:
        if result['position'] == "DQ":
            Result.objects.get_or_create(race=race,
                                  racer=Racer.objects.get(name=result['name']),
                                  bib_number=result['number'],
                                  time=result['time'],
                                  place=result['award'],
                                  dq=True)
        else:
            Result.objects.get_or_create(race=race,
                              racer=Racer.objects.get(name=result['name']),
                              bib_number=result['number'],
                              time=result['time'],
                              place=result['award'], )

    
def main():
    races = ["sanders-saunter-inaugural", "shoreline-shuffle-inaugural"]
    for r in races:
        race = Race.objects.get(slug=r)
        results = process_csv('lib/data/%s.csv' % r)
        process_results(race, results)

    
if __name__ == "__main__":
    main()
