# SysML v2 reference — keep v1 out of the model

Read this file when you write or review SysML. The workflow is in [SKILL.md](SKILL.md).

**Every example, keyword, and diagram type below that is labeled v1 is forbidden in artifacts this skill produces.** Translate, then write SysML v2.

## Language identity

| | SysML v1 (do not use) | SysML v2 (use this) |
| --- | --- | --- |
| Foundation | Unified Modeling Language (UML) 2 + SysML profile/stereotypes | **KerML** (Kernel Modeling Language) |
| What a “block” is | Stereotyped UML class | Does not exist — use **`part def` / `part`** |
| Main source | Proprietary tool project + XML Metadata Interchange (XMI) | **Textual SysML v2** (`.sysml`), optional views |
| Structure diagrams | Block definition diagram (BDD), internal block diagram (IBD) | Definition/usage text + SysML v2 interconnection/general views |
| Ports | Flow / proxy / full ports | **`port def` / `port`** with items and features |
| Values | Value properties, value types | **`attribute def` / `attribute`** |
| Constraints | Constraint blocks, parametrics | **`constraint def`**, `assert constraint` |
| Requirements | `«requirement»` stereotype | **`requirement def` / `requirement`** |
| Behavior | UML activities / state machines | **`action def` / `action`**, **`state def` / `state`** |
| Relationships | UML dependency + stereotypes | SysML v2 `satisfy`, `verify`, `allocate`, `connect`, `flow` |
| Specialization | UML generalization | **`:>`** (specialization), **`:>>`** (redefinition) |

When this skill says “SysML” with no version, it means **SysML v2**. Do not mix v1 and v2 in one model.

## Forbidden SysML v1 constructs

Never write these as the model (names, UML tags called stereotypes, diagram types, or file format):

- `block`, `«block»`, block definition diagram (BDD), internal block diagram (IBD)
- Part property, reference property, value property, constraint property
- Flow port, proxy port, full port, flow property, item flow (v1)
- Constraint block, parametric diagram (v1)
- `«requirement»`, `«testCase»`, `«satisfy»`, `«verify»`, `«allocate»` as UML stereotypes
- UML profile, stereotype, tagged value as the extension mechanism
- XMI / Eclipse UML2 as the source of truth
- MagicDraw/Cameo/Rhapsody **SysML v1** project conventions and element types
- Activity, sequence, or state-machine **UML/SysML v1** diagrams as system truth

If an input uses any of the above, rewrite it in SysML v2 before committing.

## v1 term → v2 construct

| SysML v1 (reject) | SysML v2 (write) |
| --- | --- |
| Block | `part def` |
| Part property | `part` (usage) |
| Reference property | `ref part` (or other `ref` usage, as appropriate) |
| Value property | `attribute` |
| Value type | `attribute def` |
| Constraint block | `constraint def` |
| Constraint property | `assert constraint` / constraint usage |
| Flow port / proxy / full port | `port def` / `port` |
| Item flow | `flow` / `message` (SysML v2) |
| Connector | `connection` / `connect` |
| Binding connector | `bind` |
| Package (UML) | `package` (KerML/SysML v2) |
| Requirement (`«requirement»`) | `requirement def` / `requirement` |
| Satisfy / verify (stereotyped dependency) | `satisfy` / `verify` (SysML v2 relationships) |
| Allocate (v1) | `allocate` (SysML v2) |
| Activity | `action def` / `action` / `perform` |
| State machine | `state def` / `state` |
| Generalization | specialization `:>` |
| Redefinition (UML) | redefinition `:>>` |
| Multiplicity on property | usage multiplicity `[n]` / `[1..*]` |
| BDD / IBD | SysML v2 textual definition/usage + views |
| Viewpoint (v1) | `viewpoint def` / `viewpoint`, `view def` / `view` |

## Required SysML v2 textual shape

Use definition/usage, not blocks. This is the expected shape (example only):

```sysml
package VehicleContext {
    private import ScalarValues::*;

    item def Fuel;

    port def FuelPort {
        in item fuel : Fuel;
    }

    part def Engine {
        attribute power : Real;
        port fuelIn : FuelPort;
    }

    part def Vehicle {
        attribute mass : Real;
        part engine : Engine;
        port fuelIn : FuelPort;
        connect fuelIn to engine.fuelIn;
        satisfy requirement : MassLimit;
    }

    requirement def MassLimit {
        doc /* Vehicle mass shall not exceed 1500. */
        subject vehicle : Vehicle;
        attribute massActual : Real;
        attribute massLimit : Real = 1500.0;
        require constraint { massActual <= massLimit }
    }
}
```

That is **not** the same language as SysML v1. Do not write v1 forms such as:

```
«block» Vehicle          // forbidden — use part def
value mass : Real        // forbidden — use attribute
flow port fuelIn         // forbidden — use port def / port
«requirement» MassLimit  // forbidden — use requirement def
BDD / IBD as source      // forbidden — use .sysml + SysML v2 views
```

## If the user or a document says “SysML v1”

1. State that this skill models in **SysML v2 only**.
2. Translate the intent with the table above.
3. Produce SysML v2 text (and SysML v2 views if needed).
4. Do not leave v1 keywords in comments, diagram titles, or file names as if they were the language.

## Standards and further reading

Prefer the Object Management Group (OMG) SysML v2 and KerML specifications over SysML v1 textbooks, UML references, or vendor v1 tutorials. When searching, include **“SysML v2”** and **KerML**. Ignore search results that are SysML 1.x / UML 2 unless you are only mapping old terms.
