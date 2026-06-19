import csv


class Register:
    def __init__(self, from_portid, from_country,
                 to_portid, to_country,
                 average_transit_days, daily_capacity_at_risk,
                 relative_capacity_at_risk):
        self.from_portid = from_portid
        self.from_country = from_country
        self.to_portid = to_portid
        self.to_country = to_country
        self.average_transit_days = float(average_transit_days)
        self.daily_capacity_at_risk = float(daily_capacity_at_risk)
        self.relative_capacity_at_risk = float(relative_capacity_at_risk)

    def __repr__(self):
        return (f"Register({self.from_portid} -> {self.to_portid}, "
                f"transit={self.average_transit_days}d)")


def parse(row):
    """Parse a CSV row (list of strings) into a Register instance.

    Expected column order (from dataset.csv):
    from_portid[0], from_portname[1], from_country[2], from_iso3[3], from_lat[4], from_lon[5],
    to_portid[6], to_portname[7], to_country[8], to_iso3[9], to_lat[10], to_lon[11],
    average_transit_days[12], daily_capacity_at_risk[13], relative_capacity_at_risk[14], ObjectId[15]
    """
    return Register(
        from_portid=row[0],
        from_country=row[2],
        to_portid=row[6],
        to_country=row[8],
        average_transit_days=row[12],
        daily_capacity_at_risk=row[13],
        relative_capacity_at_risk=row[14],
    )


def write_transit_SQL_from_csv(data_path, output_path, tname):
    with open(data_path, "r") as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        while reader:
            reg = parse(reader)
            with open(output_path, "w") as sql:
                sql.write(f"Insert into {tname} ({reg.from_portid},{reg.from_country},{reg.to_portid},{reg.to_country},{reg.average_transit_days},{reg.daily_capacity_at_risk},{reg.relative_capacity_at_risk}) values\n")
            next(reader, None)

if __name__ == "__main__":
    write_transit_SQL_from_csv("../data/dataset.csv", "bulk.sql", "Transit")