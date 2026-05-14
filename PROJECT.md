PROJECT DESCRIPTION + GUARDRAILS (LEARNING PROJECT)

PURPOSE OF THIS PROJECT
This project is a learning-first backend system built with Django.
The goal is not to build a production SaaS product. The goal is to deeply understand:


Django backend architecture


Multi-tenant system design


Django REST Framework patterns


ORM performance (select_related and prefetch_related)


Service layer separation


Basic production thinking (async tasks, structure, data flow)


Every decision should prioritize understanding over complexity.

CORE PHILOSOPHY (NON-NEGOTIABLE)
Every iteration must be small enough that you fully understand every line of code added.
This means:


No large feature bundles


No premature abstraction layers


No overengineering or “clean architecture for the sake of it”


No hidden logic or magic behavior


No complex frameworks inside the project


If a change cannot be explained clearly in a few sentences, it is too large.

SYSTEM SCOPE (KEEP IT SMALL)
The system only includes:
Core entities:


Organisation (tenant)


User (belongs to organisation)


Note (belongs to organisation)


Core features:


JWT authentication


CRUD API for notes


Strict tenant isolation


Basic service layer


Basic ORM optimization


Nothing beyond this should be added unless explicitly necessary for learning.

EXPLICIT NON-GOALS (DO NOT BUILD THESE)
Do NOT introduce:


Microservices


Event-driven architecture


Plugin systems


Over-engineered domain abstractions


Complex RBAC systems


Kubernetes or infrastructure complexity


Generic reusable frameworks inside the project


Over-abstracted “enterprise architecture” patterns


This is a Django learning project, not a platform design exercise.

MULTI-TENANCY RULE (CRITICAL)
All data access MUST be scoped to the current organisation.
Every query must enforce:
Only return data belonging to request.org
Allowed patterns:


Model.objects.filter(organisation=request.org)


Custom manager method like Model.objects.for_org(request.org)


Forbidden patterns:


Model.objects.all() in API layer


Any query that does not explicitly enforce organisation filtering


Trusting client input for tenant selection


If tenant isolation is unclear, stop and fix it immediately before continuing.

ARCHITECTURE RULES


Views must stay thin
Views should only:




Receive request


Call service layer


Return response


No business logic inside views.



Business logic lives in services
All non-trivial logic must live in service classes.


Example:


NoteService.create_note()


NoteService.update_note()


Do NOT place business logic in:


Views


Serializers


Models (except very small helpers)





ORM usage must be intentional
Always consider:




Could this create N+1 queries?


Should select_related be used?


Should prefetch_related be used?


Do not optimize prematurely, but do not ignore query efficiency.

ITERATION RULES (VERY IMPORTANT)
Each iteration must:


Introduce only ONE small concept at a time


Be fully understandable in isolation


Valid iterations:


Add Note model


Add JWT authentication


Add organisation filtering


Add NoteService layer


Optimize note list query


Invalid iterations:


Build full auth + notes + permissions system at once


Refactor entire architecture in one step


Add multiple unrelated features together



SAFE BUILD ORDER (FOLLOW THIS SEQUENCE)
Phase 1: Foundations


Django setup


Organisation model


User model


Basic authentication


Phase 2: Core feature


Note model


CRUD API


Tenant isolation enforcement


Phase 3: Structure


Service layer introduction


Queryset managers


Permissions cleanup


Phase 4: Quality improvements


ORM optimization (select_related, prefetch_related)


Basic tests


Edge cases


Phase 5 (optional):


Simple Celery async task



TESTING RULE (MINIMAL BUT REAL)
Tests should only verify:


Users cannot access other organisations’ data


Basic CRUD functionality works


Tenant isolation is enforced correctly


Do not aim for high test coverage. Aim for meaningful test coverage.

DEBUGGING MINDSET
When something breaks, check in this order:


Tenant filtering logic


Queryset correctness


Service layer logic


API layer logic


Most bugs will come from incorrect data scoping or missing organisation filtering.

CODE CLARITY RULES
Prefer:


Explicit code over clever code


Simple functions over abstract frameworks


Readability over micro-optimizations


If code feels clever but hard to follow, it is wrong for this project.

SUCCESS CRITERIA
You are successful if:


You can explain every file without confusion


You understand how tenant isolation works end-to-end


You can trace a request from API to database and back


You can extend functionality without breaking isolation


You can predict query behavior before running it



FINAL PRINCIPLE
The goal is not speed.
The goal is controlled, incremental complexity where every step is understood.
If the system becomes hard to reason about, you are moving too fast.