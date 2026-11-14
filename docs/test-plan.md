# Test Plan

# Testing Vikunja Task Management

**This project aims to evaluate selected functionality of the Vikunja task and project management application through manual testing, API testing, database testing and UI automation.**

## In scope

- **login**
    - Username/email field
    - password field
    - Stay logged in feature
- Project
    - project creation.
    - Edit a project.
    - Project deletion.
- Tasks
    - Task creation.
    - Task details.
    - Editing title and description.
    - Task completion and reopening.
    - Task deletion.

## Out scope

- Complete application testing.
- Performance, load and stress testing.
- Mobile application testing.
- Third-party integrations and advanced features outside the selected workflows.

## Testing Approach

- Exploratory testing.
- Manual functional testing.
- Positive and negative testing.
- API testing using Postman.
- UI end-to-end automation using Playwright.

## Entry Criteria

- Application and database are available.
- Relevant documentation has been reviewed.
- Required test data are available.

## Exist Criteria

- Planned tests have been executed.
- Identified defects have been recorded.
- Test execution results have been summarized.

## Risks and Limitations

- Internal business requirements and acceptance criteria have not been provided.
- Public documentation may not cover every business rule.
- The local environment may not represent every aspect of a production deployment.

## Environments

- **Operating system:** Windows 11
- **Application:** Vikunja 2.7.1   [http://localhost:3456](http://localhost:3456/)
- **Database:** PostgreSQL 18