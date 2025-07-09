# Reproducing the “Cut In” Scenario in CARLA Scenario Runner

## 1. Executive Summary

- **Objective:** Load and execute a “Cut In” scenario (an `.xosc` file based on the OpenSCENARIO standard) in CARLA Scenario Runner.
- **Problem:** During loading, the XML file is repeatedly rejected by the XSD validator or has non-compliant nodes stripped out, preventing the scenario from being parsed and executed correctly.
- **Approach:** Diagnose common validation failures (namespaces, missing required child elements, tag mismatches, etc.); explain in detail how the XSD validator works and how Scenario Runner applies it; then apply targeted edits to the `.xosc` file so that it passes validation and runs as intended.

## 2. Background and Requirements

CARLA Scenario Runner includes initial support for OpenSCENARIO 1.0. Its official examples (e.g. `FollowLeadingVehicle.xosc`, `PedestrianCrossing.xosc`) work out of the box. However, when attempting to load a custom “Cut In” scenario, we frequently encounter errors such as:

```
xmlschema.validators.exceptions.XMLSchemaChildrenValidationError: … Tag (BoundingBox | Performance | Axles | Properties) expected.
```

or

```
Reason: Unexpected child with tag ‘SpeedActionType’ at position 1.
Schema: … only accepts <SpeedAction> or <LongitudinalDistanceAction>.
```

All of these originate from the XSD schema’s strict constraints on the XML structure. Any deviation from the schema causes the validator to block parsing, so Scenario Runner cannot proceed.

## 3. XSD Validator Workflow

1. **Loading the schema**  
   Scenario Runner reads its schema from `srunner/scenarioconfigs/OpenSCENARIO.xsd` (or from a user-specified `xsi:schemaLocation`). That XSD—either the official ASAM/OpenSCENARIO version or a CARLA-provided simplified variant—defines, for every element, which child elements are allowed, their order, optionality, attribute types, etc.

2. **Parsing the XML document**  
   The `xmlschema` library parses the `.xosc` file into a DOM tree. Depending on the presence or absence of a namespace declaration, it may enable or skip schema validation.

3. **Schema matching and rule enforcement**  
   For each element in the DOM:
   - **Required-element checks:** If the XSD says `minOccurs="1"` but the element is missing, validation fails.
   - **Name checks:** Tag names must match exactly (case-sensitive) those defined in the XSD; any unknown tag is rejected.
   - **Type checks:** Attribute values must conform to their declared simple types (e.g. `xsd:double`, `xsd:unsignedShort`, or custom enumerations).
   - **Namespace matching:** If the XML declares a namespace, the validator matches elements against that namespace’s schema; if no namespace is declared, it uses a no-namespace schema.

4. **Error throwing**  
   As soon as any node violates its XSD constraints, `xmlschema` raises an `XMLSchemaValidationError` (often a subtype like `XMLSchemaChildrenValidationError`) and halts further validation. Scenario Runner catches that exception and aborts loading.

## 4. Common Validation Failures

| **Error Type**             | **Example Message**                                                                            | **Root Cause**                                                                                                         |
|----------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Missing required children  | “Tag (BoundingBox \| Performance \| Axles \| Properties) expected.”                           | The `<Vehicle>` element is defined in the schema to require all four child elements, but some or all are absent.       |
| Tag name mismatch          | “Unexpected child with tag ‘SpeedActionType’ at position 1.”                                   | The schema says `<LongitudinalAction>` may only contain `<SpeedAction>` or `<LongitudinalDistanceAction>`, so a custom `<SpeedActionType>` is rejected. |
| Namespace conflict         | “namespace … not loaded” error                                                                | The XML declares `xmlns="http://www.asam.net/Schemas/OpenSCENARIO"`, but Scenario Runner did not load an XSD for that namespace, so no schema is found.     |
| Type mismatch              | Attribute value out of range or wrong format                                                   | The XSD enforces strict base types (e.g. `xsd:dateTime`, `xsd:double`, enumerations); any value that doesn’t match will fail. |

---

This README summarizes the key findings and fixes needed to successfully reproduce a “Cut In” scenario in CARLA Scenario Runner.
