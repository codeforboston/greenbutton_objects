"""
These are enum objects that don't have descriptive values in the original
XSD file,  these types are created by LLM using the following prompt:

```
Transform this into into a Enum class and a dictionary

Dictionary should contain mapping between numeric enum value and the text description.
Enum class should be equivalent to the original class but have descrptive abreveations
for the values instead of simple VALUE_0

Include references to the original class.

Also add a enum constant that represents a missing value
```


TODO:  Would be interesting to put it into CI/CD


"""

from enum import Enum


class ServiceKind(Enum):
    """
    Enum representing the type of service.
    Equivalent to the original ServiceKindValue class.
    """

    ELECTRICITY = 0
    GAS = 1
    WATER = 2
    TIME = 3
    HEAT = 4
    REFUSE = 5
    SEWERAGE = 6
    RATES = 7
    TV_LICENSE = 8
    INTERNET = 9
    MISSING = -1


SERVICE_KIND_DESCRIPTIONS = {
    ServiceKind.ELECTRICITY.value: "Electricity service.",
    ServiceKind.GAS.value: "Gas service.",
    ServiceKind.WATER.value: "Water service.",
    ServiceKind.TIME.value: "Time service.",
    ServiceKind.HEAT.value: "Heat service.",
    ServiceKind.REFUSE.value: "Refuse (waster) service.",
    ServiceKind.SEWERAGE.value: "Sewerage service.",
    ServiceKind.RATES.value: "Rates (e.g. tax, charge, toll, duty, tariff, etc.) service.",
    ServiceKind.TV_LICENSE.value: "TV license service.",
    ServiceKind.INTERNET.value: "Internet service.",
    ServiceKind.MISSING.value: "Missing service kind value.",
}


class QualityOfReading(Enum):
    """
    Enum representing the quality of a reading.
    Equivalent to the original QualityOfReadingValue class.
    """

    VALIDATED = 0
    HUMAN_APPROVED = 7
    MACHINE_COMPUTED = 8
    INTERPOLATED = 9
    FAILED_CHECKS = 10
    CALCULATED = 11
    FORECASTED = 12
    MIXED_QUALITY = 13
    UNVALIDATED = 14
    WEATHER_ADJUSTED = 15
    OTHER = 16
    APPROVED_EDITED = 17
    FAILED_BUT_ACTUAL = 18
    BILLING_ACCEPTABLE = 19
    MISSING = -1


QUALITY_OF_READING_DESCRIPTIONS = {
    QualityOfReading.VALIDATED.value: "data that has gone through all required validation checks "
    "and either passed them all or has been verified",
    QualityOfReading.HUMAN_APPROVED.value: "Replaced or approved by a human",
    QualityOfReading.MACHINE_COMPUTED.value: "data value was replaced by a machine computed value based on "
    "analysis of historical data using the same type of measurement.",
    QualityOfReading.INTERPOLATED.value: "data value was computed using linear "
    "interpolation based on the readings before and after it",
    QualityOfReading.FAILED_CHECKS.value: "data that has failed one or more checks",
    QualityOfReading.CALCULATED.value: "data that has been calculated "
    "(using logic or mathematical operations)",
    QualityOfReading.FORECASTED.value: "data that has been calculated "
    "as a projection or forecast of future readings",
    QualityOfReading.MIXED_QUALITY.value: "indicates that the quality of "
    "this reading has mixed characteristics",
    QualityOfReading.UNVALIDATED.value: "data that has not gone through the validation",
    QualityOfReading.WEATHER_ADJUSTED.value: "the values have been adjusted " "to account for weather",
    QualityOfReading.OTHER.value: "specifies that a characteristic applies other " "than those defined",
    QualityOfReading.APPROVED_EDITED.value: "data that has been validated and "
    "possibly edited and/or estimated in accordance with approved procedures",
    QualityOfReading.FAILED_BUT_ACTUAL.value: "data that failed at least one of "
    "the required validation checks but was determined to represent actual usage",
    QualityOfReading.BILLING_ACCEPTABLE.value: "data that is valid and acceptable " "for billing purposes",
    QualityOfReading.MISSING.value: "Missing quality of reading value.",
}


class UnitSymbol(Enum):
    """
    Enum representing the unit symbol values.
    Equivalent to the original UnitSymbol class.
    """

    VA = 61
    W = 38
    VAR = 63
    VAH = 71
    WH = 72
    VARH = 73
    V = 29
    OHM = 30
    A = 5
    FARAD = 25
    HENRY = 28
    DEG_C = 23
    S = 27
    MIN = 159
    H = 160
    DEG = 9
    RAD = 10
    J = 31
    N = 32
    SIEMENS = 53
    NONE = 0
    HZ = 33
    G = 3
    PA = 39
    M = 2
    M2 = 41
    M3 = 42
    A2 = 69
    A2H = 105
    A2S = 70
    AH = 106
    A_PER_A = 152
    A_PER_M = 103
    AS = 68
    B_SPL = 79
    BM = 113
    BQ = 22
    BTU = 132
    BTU_PER_H = 133
    CD = 8
    CHAR = 76
    HZ_PER_S = 75
    CODE = 114
    COS_PHI = 65
    COUNT = 111
    FT3 = 119
    FT3_COMPENSATED = 120
    FT3_COMPENSATED_PER_H = 123
    GM2 = 78
    G_PER_G = 144
    GY = 21
    HZ_PER_HZ = 150
    CHAR_PER_S = 77
    IMPERIAL_GAL = 130
    IMPERIAL_GAL_PER_H = 131
    J_PER_K = 51
    J_PER_KG = 165
    K = 6
    KAT = 158
    KG_M = 47
    G_PER_M3 = 48
    L = 134
    L_COMPENSATED = 157
    L_COMPENSATED_PER_H = 138
    L_PER_H = 137
    L_PER_L = 143
    L_PER_S = 82
    L_UNCOMPENSATED = 156
    L_UNCOMPENSATED_PER_H = 139
    LM = 35
    LX = 34
    M2_PER_S = 49
    M3_COMPENSATED = 167
    M3_COMPENSATED_PER_H = 126
    M3_PER_H = 125
    M3_PER_S = 45
    M3_UNCOMPENSATED = 166
    M3_UNCOMPENSATED_PER_H = 127
    ME_CODE = 118
    MOL = 7
    MOL_PER_KG = 147
    MOL_PER_M3 = 145
    MOL_PER_MOL = 146
    CURRENCY = 80
    M_PER_M = 148
    M_PER_M3 = 46
    M_PER_S = 43
    M_PER_S2 = 44
    OHM_M = 102
    PA_A = 155
    PA_G = 140
    PSI_A = 141
    PSI_G = 142
    Q = 100
    Q45 = 161
    Q45H = 163
    Q60 = 162
    Q60H = 164
    QH = 101
    RAD_PER_S = 54
    REV = 154
    REV_PER_S = 4
    S_PER_S = 149
    SR = 11
    STATUS = 109
    SV = 24
    T = 37
    THERM = 169
    TIMESTAMP = 108
    US_GAL = 128
    US_GAL_PER_H = 129
    V2 = 67
    V2H = 104
    VAH_PER_REV = 117
    VARH_PER_REV = 116
    V_PER_HZ = 74
    V_PER_V = 151
    VS = 66
    WB = 36
    WH_PER_M3 = 107
    WH_PER_REV = 115
    W_PER_M_K = 50
    W_PER_S = 81
    W_PER_VA = 153
    W_PER_W = 168
    MISSING = -1


UNIT_SYMBOL_DESCRIPTIONS = {
    UnitSymbol.VA.value: "Apparent power, Volt Ampere (See also real power and " "reactive power.), VA",
    UnitSymbol.W.value: "Real power, Watt. By definition, one Watt equals one "
    "Joule per second. Electrical power may have real and reactive "
    "components. The real portion of electrical power (I²R) or VIcos?, is "
    "expressed in Watts. (See also apparent power and reactive power.), W",
    UnitSymbol.VAR.value: "Reactive power, Volt Ampere reactive. The "
    '"reactive" or "imaginary" component of electrical power (VISin?). '
    "(See also real power and apparent power)., VAr",
    UnitSymbol.VAH.value: "Apparent energy, Volt Ampere hours, VAh",
    UnitSymbol.WH.value: "Real energy, Watt hours, Wh",
    UnitSymbol.VARH.value: "Reactive energy, Volt Ampere reactive hours, VArh",
    UnitSymbol.V.value: "Electric potential, Volt (W/A), V",
    UnitSymbol.OHM.value: "Electric resistance, Ohm (V/A), O",
    UnitSymbol.A.value: "Current, ampere, A",
    UnitSymbol.FARAD.value: "Electric capacitance, Farad (C/V), °C",
    UnitSymbol.HENRY.value: "Electric inductance, Henry (Wb/A), H",
    UnitSymbol.DEG_C.value: "Relative temperature in degrees Celsius. In the SI "
    "unit system the symbol is ºC. Electric charge is measured in coulomb "
    "that has the unit symbol C. To distinguish degree Celsius from "
    "coulomb the symbol used in the UML is degC. Reason for not using ºC "
    "is the special character º is difficult to manage in software.",
    UnitSymbol.S.value: "Time, seconds, s",
    UnitSymbol.MIN.value: "Time, minute = s * 60, min",
    UnitSymbol.H.value: "Time, hour = minute * 60, h",
    UnitSymbol.DEG.value: "Plane angle, degrees, deg",
    UnitSymbol.RAD.value: "Plane angle, Radian (m/m), rad",
    UnitSymbol.J.value: "Energy joule, (N·m = C·V = W·s), J",
    UnitSymbol.N.value: "Force newton, (kg m/s²), N",
    UnitSymbol.SIEMENS.value: "Electric conductance, Siemens (A / V = 1 / O), S",
    UnitSymbol.NONE.value: "N/A, None",
    UnitSymbol.HZ.value: "Frequency hertz, (1/s), Hz",
    UnitSymbol.G.value: "Mass in gram, g",
    UnitSymbol.PA.value: "Pressure, Pascal (N/m²)(Note: the absolute or "
    "relative measurement of pressure is implied with this entry. See "
    "below for more explicit forms.), Pa",
    UnitSymbol.M.value: "Length, meter, m",
    UnitSymbol.M2.value: "Area, square meter, m²",
    UnitSymbol.M3.value: "Volume, cubic meter, m³",
    UnitSymbol.A2.value: "Amps squared, amp squared, A2",
    UnitSymbol.A2H.value: "ampere-squared, Ampere-squared hour, A²h",
    UnitSymbol.A2S.value: "Amps squared time, square amp second, A²s",
    UnitSymbol.AH.value: "Ampere-hours, Ampere-hours, Ah",
    UnitSymbol.A_PER_A.value: "Current, Ratio of Amperages, A/A",
    UnitSymbol.A_PER_M.value: "A/m, magnetic field strength, Ampere per metre, A/m",
    UnitSymbol.AS.value: "Amp seconds, amp seconds, As",
    UnitSymbol.B_SPL.value: "Sound pressure level, Bel, acoustic, Combine with "
    '\'multiplier prefix "d" to form decibels of Sound Pressure Level db'
    "(SPL), B (SPL)",
    UnitSymbol.BM.value: "Signal Strength, Bel-mW, normalized to 1mW. Note: to "
    'form "dBm" combine "Bm" with multiplier "d". Bm',
    UnitSymbol.BQ.value: "Radioactivity, Becquerel (1/s), Bq",
    UnitSymbol.BTU.value: "Energy, British Thermal Units, BTU",
    UnitSymbol.BTU_PER_H.value: "Power, BTU per hour, BTU/h",
    UnitSymbol.CD.value: "Luminous intensity, candela, cd",
    UnitSymbol.CHAR.value: "Number of characters, characters, char",
    UnitSymbol.HZ_PER_S.value: "Rate of change of frequency, hertz per second, Hz/s",
    UnitSymbol.CODE.value: "Application Value, encoded value, code",
    UnitSymbol.COS_PHI.value: "Power factor, Dimensionless, cos?",
    UnitSymbol.COUNT.value: "Amount of substance, counter value, count",
    UnitSymbol.FT3.value: "Volume, cubic feet, ft³",
    UnitSymbol.FT3_COMPENSATED.value: "Volume, cubic feet, ft³(compensated)",
    UnitSymbol.FT3_COMPENSATED_PER_H.value: "Volumetric flow rate, "
    "compensated cubic feet per hour, ft³(compensated)/h",
    UnitSymbol.GM2.value: "Turbine inertia, gram·meter2 (Combine with "
    'multiplier prefix "k" to form kg·m2.), gm²',
    UnitSymbol.G_PER_G.value: "Concentration, The ratio of the mass of a "
    "solute divided by the mass of the solution., g/g",
    UnitSymbol.GY.value: "Absorbed dose, Gray (J/kg), GY",
    UnitSymbol.HZ_PER_HZ.value: "Frequency, Rate of frequency change, Hz/Hz",
    UnitSymbol.CHAR_PER_S.value: "Data rate, characters per second, char/s",
    UnitSymbol.IMPERIAL_GAL.value: "Volume, imperial gallons, ImperialGal",
    UnitSymbol.IMPERIAL_GAL_PER_H.value: "Volumetric flow rate, Imperial " "gallons per hour, ImperialGal/h",
    UnitSymbol.J_PER_K.value: "Heat capacity, Joule/Kelvin, J/K",
    UnitSymbol.J_PER_KG.value: "Specific energy, Joules / kg, J/kg",
    UnitSymbol.K.value: "Temperature, Kelvin, K",
    UnitSymbol.KAT.value: "Catalytic activity, katal = mol / s, kat",
    UnitSymbol.KG_M.value: "Moment of mass ,kilogram meter (kg·m), M",
    UnitSymbol.G_PER_M3.value: "Density, gram/cubic meter (combine with prefix "
    'multiplier "k" to form kg/ m³), g/m³',
    UnitSymbol.L.value: "Volume, litre = dm3 = m3/1000., L",
    UnitSymbol.L_COMPENSATED.value: "Volume, litre, with the value "
    "compensated for weather effects, L(compensated)",
    UnitSymbol.L_COMPENSATED_PER_H.value: "Volumetric flow rate, litres "
    "(compensated) per hour, L(compensated)/h",
    UnitSymbol.L_PER_H.value: "Volumetric flow rate, litres per hour, L/h",
    UnitSymbol.L_PER_L.value: "Concentration, The ratio of the volume of a "
    "solute divided by the volume of the solution., L/L",
    UnitSymbol.L_PER_S.value: "Volumetric flow rate, Volumetric flow rate, L/s",
    UnitSymbol.L_UNCOMPENSATED.value: "Volume, litre, with the value "
    "uncompensated for weather effects., L(uncompensated)",
    UnitSymbol.L_UNCOMPENSATED_PER_H.value: "Volumetric flow rate, litres "
    "(uncompensated) per hour, L(uncompensated)/h",
    UnitSymbol.LM.value: "Luminous flux, lumen (cd sr), Lm",
    UnitSymbol.LX.value: "Illuminance lux, (lm/m²), L(uncompensated)/h",
    UnitSymbol.M2_PER_S.value: "Viscosity, meter squared / second, m²/s",
    UnitSymbol.M3_COMPENSATED.value: "Volume, cubic meter, with the value "
    "compensated for weather effects., m3(compensated)",
    UnitSymbol.M3_COMPENSATED_PER_H.value: "Volumetric flow rate, "
    "compensated cubic meters per hour, ³(compensated)/h",
    UnitSymbol.M3_PER_H.value: "Volumetric flow rate, cubic meters per hour, m³/h",
    UnitSymbol.M3_PER_S.value: "m3PerSec, cubic meters per second, m³/s",
    UnitSymbol.M3_UNCOMPENSATED.value: "m3uncompensated, cubic meter, with "
    "the value uncompensated for weather effects., m3(uncompensated)",
    UnitSymbol.M3_UNCOMPENSATED_PER_H.value: "Volumetric flow rate, "
    "uncompensated cubic meters per hour, m³(uncompensated)/h",
    UnitSymbol.ME_CODE.value: "EndDeviceEvent, value to be interpreted as a " "EndDeviceEventCode, meCode",
    UnitSymbol.MOL.value: "Amount of substance, mole, mol",
    UnitSymbol.MOL_PER_KG.value: "Concentration, Molality, the amount of "
    "solute in moles and the amount of solvent in kilograms., mol/kg",
    UnitSymbol.MOL_PER_M3.value: "Concentration, The amount of substance "
    "concentration, (c), the amount of solute in moles divided by the "
    "volume of solution in m³., mol/m³",
    UnitSymbol.MOL_PER_MOL.value: "Concentration, Molar fraction (x), the "
    "ratio of the molar amount of a solute divided by the molar amount of "
    "the solution., mol/mol",
    UnitSymbol.CURRENCY.value: "Monetary unit, Generic money (Note: Specific "
    "monetary units are identified by the currency class)., ¤",
    UnitSymbol.M_PER_M.value: "Length, Ratio of length, m/m",
    UnitSymbol.M_PER_M3.value: "Fuel efficiency, meters per cubic meter, m/m³",
    UnitSymbol.M_PER_S.value: "Velocity, meters per second, m/s",
    UnitSymbol.M_PER_S2.value: "Acceleration, meters per second squared, m/s²",
    UnitSymbol.OHM_M.value: "Resistivity, ohm meter, Ω·m",
    UnitSymbol.PA_A.value: "Pressure, Pascal absolute, PaA",
    UnitSymbol.PA_G.value: "Pressure, Pascal gauge, PaG",
    UnitSymbol.PSI_A.value: "Pressure, Pounds per square inch absolute, psiA",
    UnitSymbol.PSI_G.value: "Pressure, Pounds per square inch gauge, psiG",
    UnitSymbol.Q.value: "Quantity power, Q, Q",
    UnitSymbol.Q45.value: "Quantity power, Q measured at 45°, Q45",
    UnitSymbol.Q45H.value: "Quantity energy, Q measured at 45°, Q45h",
    UnitSymbol.Q60.value: "Quantity power, Q measured at 60°, Q60",
    UnitSymbol.Q60H.value: "Quantity energy, Qh measured at 60°, Q60h",
    UnitSymbol.QH.value: "Quantity energy, Qh, Qh",
    UnitSymbol.RAD_PER_S.value: "Angular velocity, radians per second, rad/s",
    UnitSymbol.REV.value: "Amount of rotation, Revolutions, rev",
    UnitSymbol.REV_PER_S.value: "Rotational speed, Revolutions per second, rev/s",
    UnitSymbol.S_PER_S.value: "Time, Ratio of time (can be combined with a "
    "multiplier prefix to show rates such as a clock drift rate, e.g. "
    '"µs/s"), s/s',
    UnitSymbol.SR.value: "Solid angle, Steradian, sr",
    UnitSymbol.STATUS.value: 'State, "1" = "true", "live", "on", "high", '
    '"set"; "0" = "false", "dead", "off", "low", "cleared". Note: A '
    "Boolean value is preferred but other values may be supported, status",
    UnitSymbol.SV.value: "Dose equivalent, Sievert, Sv",
    UnitSymbol.T.value: "Magnetic flux density, Tesla, T",
    UnitSymbol.THERM.value: "Energy, Therm, therm",
    UnitSymbol.TIMESTAMP.value: "Timestamp, time and date per ISO 8601 " "format, timeStamp",
    UnitSymbol.US_GAL.value: "Volume, US gallons, USGal",
    UnitSymbol.US_GAL_PER_H.value: "Volumetric flow rate, US gallons per " "hour, USGal/h",
    UnitSymbol.V2.value: "Volts squared, Volt squared, V²",
    UnitSymbol.V2H.value: "Volt-squared hour, Volt-squared-hours, V²h",
    UnitSymbol.VAH_PER_REV.value: "Apparent energy metering constant, VAh per " "revolution, VAh/rev",
    UnitSymbol.VARH_PER_REV.value: "Reactive energy metering constant, VArh " "per revolution, VArh/rev",
    UnitSymbol.V_PER_HZ.value: "Magnetic flux, Volts per Hertz, V/Hz",
    UnitSymbol.V_PER_V.value: "Voltage, Ratio of voltages (e.g. mV/V), V/V",
    UnitSymbol.VS.value: "Volt seconds, Volt seconds, Vs",
    UnitSymbol.WB.value: "Magnetic flux, Weber, Wb",
    UnitSymbol.WH_PER_M3.value: "Energy per volume, Watt-hours per cubic " "meter, Wh/m³",
    UnitSymbol.WH_PER_REV.value: "Active energy metering constant, Wh per " "revolution, Wh/rev",
    UnitSymbol.W_PER_M_K.value: "Thermal conductivity, Watt per meter Kelvin, " "W/(m·K)",
    UnitSymbol.W_PER_S.value: "Ramp rate, Watts per second, W/s",
    UnitSymbol.W_PER_VA.value: "Power Factor, PF, W/VA",
    UnitSymbol.W_PER_W.value: "Signal Strength, Ratio of power, W/W",
    UnitSymbol.MISSING.value: "Unknown unit value, Unknown, unknown",
}
